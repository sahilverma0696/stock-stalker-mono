import threading
from stock_stalker.basic import LOG
from internal.utility.modules.yfinance.fetch import fetchData
from datetime import datetime
from django.http import JsonResponse





# TODO: Make the response return correct in this
# Define a threading.Event to signal when the background thread is done
thread_done = threading.Event()


def fetch_data(request):
    date_string = request.GET.get('date', None)

    # Define a dictionary to store the response data
    response_data = {'success': False, 'message': 'default'}

    def fetch_data_threaded():
        try:
            nonlocal response_data  # Allow modification of the outer response_data variable
            if date_string is not None:
                date = datetime.strptime(date_string, '%Y-%m-%d')
                fetchData(date)
                response_data = {
                    'success': True, 'message': 'Data fetch started, from your provided date'}
            else:
                fetchData()
                response_data = {
                    'success': True, 'message': 'Data fetch started, from default date'}
        except Exception as e:
            LOG.error("%s", e)
            response_data = {'success': False,
                             'message': f'internal server error'}
        finally:
            # Set the threading.Event to indicate that the thread is done
            thread_done.set()

    # Create a thread and start it
    fetch_thread = threading.Thread(target=fetch_data_threaded)
    fetch_thread.start()

    # Return a response immediately
    return JsonResponse(response_data)

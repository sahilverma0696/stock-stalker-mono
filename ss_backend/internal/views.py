# from django.db.models import Max
# from internal.stocksdata.models import StockData
# from datetime import datetime
# from django.http import JsonResponse
# import json
# import logging


# # logger = logging.getLogger(__name__)

# # # Create your views here.
# # def getDate(pSymbol):
# #     """Returns the last recent data from which data needed to be fetched"""
# #     ## YYYY-MM-DD
# #     latest_date = datetime(2015, 1, 1)

# #     # Check if data for "SBIN" exists in the model
# #     if StockData.objects.filter(symbol=pSymbol).exists():
# #         latest_date = StockData.get_latest_date_from_db(pSymbol)

# #     return latest_date


# # from internal.utility.yfinance.fetch import fetchData

# # import threading
# # from datetime import datetime


# # #TODO: Make the response return correct in this
# # # Define a threading.Event to signal when the background thread is done
# # thread_done = threading.Event()

# # def fetch_data(request):
# #     date_string = request.GET.get('date', None)

# #     # Define a dictionary to store the response data
# #     response_data = {'success': False, 'message': 'default'}

# #     def fetch_data_threaded():
# #         try:
# #             nonlocal response_data  # Allow modification of the outer response_data variable
# #             if date_string is not None:
# #                 date = datetime.strptime(date_string, '%Y-%m-%d')
# #                 fetchData(date)
# #                 response_data = {'success': True, 'message': 'Data fetch started, from your provided date'}
# #             else:
# #                 fetchData()
# #                 response_data = {'success': True, 'message': 'Data fetch started, from default date'}
# #         except Exception as e:
# #             logger.error("%s", e)
# #             response_data = {'success': False, 'message': f'internal server error'}
# #         finally:
# #             # Set the threading.Event to indicate that the thread is done
# #             thread_done.set()

# #     # Create a thread and start it
# #     fetch_thread = threading.Thread(target=fetch_data_threaded)
# #     fetch_thread.start()

# #     # Return a response immediately
# #     return JsonResponse(response_data)

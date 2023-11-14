import json
from django.http import JsonResponse

def calculate_sma_view(request):
    if request.method == 'GET':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))

            symbol_list = data.get('symbol_list', [])
            window_size = data.get('window_size', 10)
            days_to_check = data.get('days_to_check', 5)
            trend_type = data.get('trend_type', 'exact')
            increasing = data.get('increasing', False)

            # filter_stocks(symbol_list, window_size, "increasing", days_to_check, trend_type)
            result = []
            response_data = {'success': True, 'result': result}
        except Exception as e:
            response_data = {'success here': False, 'message': str(e)}
    else:
        response_data = {'success': False, 'message': 'Invalid request method'}

    return JsonResponse(response_data)

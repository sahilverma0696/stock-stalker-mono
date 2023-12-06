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

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([AllowAny, IsAuthenticatedOrReadOnly])
def executeIndicator(request):

    '''
    # Take the list of symbols, or watchlist name from the request 
    # extract indicator conditions and stuct 
    # example SMA :{condition1,condition2}, EMA :{condition1,condition2}
    # use this key to point to the right function Application layer
    # App layer will call the indicators core layer to get the insights
    # return pruned list

    API layer:      [symbols]
    Assembler layer:[symbols], [smybol]->df, []result
    Appilication layer:[symbols], [smybol]->df, []result
    Core layer : [symbols], [smybol]->df, []result
    
    '''

    return
    

    


from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
import json
from django.http import JsonResponse
from rest_framework.response import Response


from internal.indicators.modules.dataframes import getDataFrameMap
from internal.indicators.modules.mapper import IndicatorMap
from internal.indicators.modules.moving_average import evaluate_sma


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


@api_view(["POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([AllowAny, IsAuthenticatedOrReadOnly])
# TODO:This is allowed by logged it-> free tier and paid folks
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

    """
    REQUEST STRUCT :
    map[indicator]:{
    
    }
    """
    data = request.data

    # Extract the list of strings
    string_list = data.get("stocks")

    # Check if the key exists and the value is a list
    if not string_list or not isinstance(string_list, list):
        raise ValueError("Missing or invalid string list")

    # Process the list of strings
    for string in string_list:
        # Do something with the string
        print(string)

    return JsonResponse("Success")


# Define your indicator models and related logic here


@api_view(["POST"])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([AllowAny, IsAuthenticated])
def indicator(request):
    """
    Create and apply indicators based on request body data.
    """

    # Get data from request body
    try:
        indicators = request.data["indicators"]
        symbols = request.data["symbols"]
    except KeyError:
        return JsonResponse(
            {"error": "Missing required keys in request body."}, status=400
        )

    # Validate data format
    if not isinstance(indicators, dict) or not isinstance(symbols, list):
        return JsonResponse(
            {"error": "Invalid data format."}, status=400
        )

    dfMap = getDataFrameMap(symbols,200)
    
    for _,df in dfMap.items():
        for indicator_name, properties in indicators.items():
            indicatorFunc = IndicatorMap[indicator_name]
            ## this automatically takes the properties mapping, kwargs not needed
            indicatorFunc(df,**properties)

    print(dfMap)



    # Return success response
    return JsonResponse(
        {"message": "Indicators successfully created and applied."}, status=201
    )



@api_view(["POST"])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([AllowAny, IsAuthenticated])
def maSlopeAnalysis(request):
    """
    Returns a list of symbols which stands true for the given MA slope conditions

    Supports 1-n number of MA conditions provided
    Condition

    MA      Value       Type    Direction    From      Bars 
    EMA     44          O       INC          Min        1
    SMA     50          H       DEC          Max        2
    WMA     10          L                    Exact      3
                        C

    example:
    {
    "indicators": [{
            "name":"sma",
            "column": "close",
            "length": 50,
            "offset": 0,
            "direction":"increasing",
            "condition":"minimum",
            "bars":3
        },
        {
            "name":"sma",
            "column": "close",
            "length": 44,
            "offset": 0,
            "direction":"increasing",
            "condition":"minimum",
            "bars":3
        }
    ],
    "symbols": [
        "SBIN",
        "YESBANK"
    ]
}
    """

    # Get data from request body
    try:
        indicators = request.data["indicators"]
        symbols = request.data["symbols"]
    except KeyError:
        return JsonResponse(
            {"error": "Missing required keys in request body."}, status=400
        )

    # Validate data format
    if not isinstance(indicators, list) or not isinstance(symbols, list):
        return JsonResponse(
            {"error": "Invalid data format."}, status=400
        )
    
    result = set()

    dfMap = getDataFrameMap(symbols,200)


    for _,df in dfMap.items():
        for eachIndicator in indicators:
            indicatorFunc = IndicatorMap[eachIndicator["name"].lower()]
            indicatorFunc(df,**eachIndicator)
            ## this loop checks for each df each indicator statement on it, so all 
            ## checks are evalutated that's fine
            evaluate_sma(df,result,**eachIndicator)




    # Return success response
    return Response(data=result, status=200)

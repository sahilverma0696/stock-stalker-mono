from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,status
from django.db.models import Max
from rest_framework.views import APIView
from .models import Symbol
from .serializers import SymbolSerializer
from .models import StockData
from .serializers import StockDataSerializer
from datetime import datetime
from django.http import JsonResponse
import json



import logging


logger = logging.getLogger(__name__)

# Create your views here.
def getDate():
    """Returns the last recent data from which data needed to be fetched"""
    # TODO: remove hardcoded value of SYMBOL
    latest_date = datetime(2015, 1, 1)
   
    # Check if data for "SBIN" exists in the model
    if StockData.objects.filter(symbol='SBIN').exists():
        latest_date_query = StockData.objects.filter(symbol='SBIN').aggregate(latest_date=Max('date'))
        latest_date = latest_date_query['latest_date']
    
    return latest_date



class StockDataList(generics.ListAPIView):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer

class StockDataDetail(generics.RetrieveUpdateAPIView):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer

class StockDataCreate(generics.CreateAPIView):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer

#-----


class SymbolList(APIView):
    def get(self, request):
        symbols = Symbol.objects.all()
        serializer = SymbolSerializer(symbols, many=True)
        return Response(serializer.data)

    def post(self, request):
        symbol_data = request.data.get("symbols", [])
        
        if not symbol_data:
            return Response({"message": "No symbols provided for insertion."}, status=status.HTTP_400_BAD_REQUEST)

        unique_symbols = list(set(symbol_data))  # Deduplicate the provided symbols

        if unique_symbols:
            new_symbols = [Symbol(symbol=symbol) for symbol in unique_symbols]
            Symbol.objects.bulk_create(new_symbols)
            return Response({"message": "Symbols added successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No new symbols to add."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        symbols_to_delete = request.data.get('symbols', [])
        if not symbols_to_delete:
            return Response({"message": "No symbols provided for deletion."}, status=status.HTTP_400_BAD_REQUEST)

        symbols_deleted = Symbol.objects.filter(symbol__in=symbols_to_delete).delete()
        return Response({"message": f"{symbols_deleted[0]} symbols deleted successfully."}, status=status.HTTP_204_NO_CONTENT)



from internal.modules.yfinance.fetch import fetchData

def fetch_data(request):
    date_string = request.GET.get('date',None)

    #TODO: Make this flow in thread, since data scrapping takes time
    try:
        if date_string!= None:
            date = datetime.strptime(date_string, '%Y-%m-%d')
            fetchData(date)
            response_data = {'success': True, 'message': 'Data fetch started, from your provided date'}
        else:
            fetch_data()
            response_data = {'success': True, 'message': 'Data fetch started, from default date'}
    except Exception as e:
        logger.error("%s", e)
        response_data = {'success': False, 'message': f'internal server error'}
    
    return JsonResponse(response_data)



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

            result = [] #filter_stocks(symbol_list, window_size, "increasing", days_to_check, trend_type)
            response_data = {'success': True, 'result': result}
        except Exception as e:
            response_data = {'success here': False, 'message': str(e)}
    else:
        response_data = {'success': False, 'message': 'Invalid request method'}

    return JsonResponse(response_data)
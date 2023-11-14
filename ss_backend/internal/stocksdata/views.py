from rest_framework import generics, status
from internal.stocksdata.models import StockData
from rest_framework.response import Response
from rest_framework.views import APIView


from internal.stocksdata.serializers import StockDataSerializer

# To get all data from StockData Model
class StockDataList(generics.ListAPIView):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer

# To perform CRUD operations on StockData Model with a pk
class StockDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer

# Tp post data for StockData Model
class StockDataCreate(generics.CreateAPIView):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer


# To delete a model by symbol
class CustomStockDataDelete(generics.DestroyAPIView):
    serializer_class = StockDataSerializer

    def get_queryset(self):
        symbol = self.kwargs['symbol']  # Symbol value to match for deletion
        return StockData.objects.filter(symbol__symbol=symbol)  # Filter by symbol value

    def destroy(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# to get all data of a model by symbol
class StockDataBySymbol(generics.ListAPIView):
    serializer_class = StockDataSerializer

    def get_queryset(self):
        symbol = self.kwargs['symbol']  # Symbol value to filter by
        return StockData.objects.filter(symbol__symbol=symbol)
    
#To delete all stock data 
class DeleteAllStockData(APIView):
    def delete(self, request, *args, **kwargs):
        try:
            # Delete all records in the StockData model
            StockData.objects.all().delete()
            return Response({"message": "All data in StockData has been deleted."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
from rest_framework import generics, status
from internal.models import StockData
from rest_framework.response import Response

from internal.serializers import StockDataSerializer

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
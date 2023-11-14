from django.db import router
from django.urls import path,include
from internal.stocksdata.views import StockDataList,StockDataDetail,StockDataCreate,CustomStockDataDelete,StockDataBySymbol,DeleteAllStockData

urlpatterns = [
    path('stockdata/', StockDataList.as_view(), name='stockdata-list'),
    path('stockdata/<int:pk>/', StockDataDetail.as_view(), name='stockdata-detail'),
    path('stockdata/create/', StockDataCreate.as_view(), name='stockdata-create'),
    path('delete-stock-data/<str:symbol>/', CustomStockDataDelete.as_view(), name='custom-stock-data-delete'),
    path('delete-all-stock-data/', DeleteAllStockData.as_view(), name='delete-all-stock-data'),
    path('stockdata/<str:symbol>/', StockDataBySymbol.as_view(), name='stock-data-by-symbol'),  
]


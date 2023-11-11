from django.db import router
from django.urls import path
from internal.views_dir.symbol import SymbolList
from internal.views_dir.stockdata import StockDataList,StockDataDetail,StockDataCreate,CustomStockDataDelete,StockDataBySymbol,DeleteAllStockData
from .views import fetch_data, calculate_sma_view

#--------------------------------
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from internal.views_dir.symbol import SymbolViewSet
from internal.views_dir.watchlists import WatchListView

router = DefaultRouter()
router.register(r'symbol',SymbolViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('symbols/', SymbolList.as_view(), name='symbol-list'),

    path('stockdata/', StockDataList.as_view(), name='stockdata-list'),
    path('stockdata/<int:pk>/', StockDataDetail.as_view(), name='stockdata-detail'),
    path('stockdata/create/', StockDataCreate.as_view(), name='stockdata-create'),
    path('delete-stock-data/<str:symbol>/', CustomStockDataDelete.as_view(), name='custom-stock-data-delete'),
    path('delete-all-stock-data/', DeleteAllStockData.as_view(), name='delete-all-stock-data'),
    path('stockdata/<str:symbol>/', StockDataBySymbol.as_view(), name='stock-data-by-symbol'),

    path('watchlists/',WatchListView.as_view(),name='watchlists'),

    
    path('fetchData/', fetch_data, name='fetch-data'),

    path('calculate-sma/', calculate_sma_view, name='calculate-sma'),
    
]


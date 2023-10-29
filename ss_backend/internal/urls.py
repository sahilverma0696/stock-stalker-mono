from django.db import router
from django.urls import path
from internal.views_dir.symbol import SymbolList
from internal.views_dir.stockdata import StockDataList,StockDataDetail,StockDataCreate,CustomStockDataDelete,StockDataBySymbol
from internal.views_dir.lists import ListsListCreateView,ListsDetailView
from .views import fetch_data, calculate_sma_view

#--------------------------------
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from internal.views_dir.symbol import SymbolViewSet

router = DefaultRouter()
router.register(r'symbol',SymbolViewSet)


urlpatterns = [
    #Symbol Table
    path('',include(router.urls)),
    path('symbols/', SymbolList.as_view(), name='symbol-list'),

    # StockData table
    path('stockdata/', StockDataList.as_view(), name='stockdata-list'),
    path('stockdata/<int:pk>/', StockDataDetail.as_view(), name='stockdata-detail'),
    path('stockdata/create/', StockDataCreate.as_view(), name='stockdata-create'),
    path('delete-stock-data/<str:symbol>/', CustomStockDataDelete.as_view(), name='custom-stock-data-delete'),
    path('stock-data/<str:symbol>/', StockDataBySymbol.as_view(), name='stock-data-by-symbol'),

    #Lists Table
    path('lists/', ListsListCreateView.as_view(), name='lists-list-create'),
    path('lists/<int:pk>/', ListsDetailView.as_view(), name='lists-detail'),


    path('fetchData/', fetch_data, name='fetch-data'),

    path('calculate-sma/', calculate_sma_view, name='calculate-sma'),
    
]


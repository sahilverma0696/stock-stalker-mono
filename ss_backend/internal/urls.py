from django.urls import path
from .views import StockDataList, StockDataDetail, StockDataCreate, SymbolList, fetch_data, calculate_sma_view

urlpatterns = [
    path('stockdata/', StockDataList.as_view(), name='stockdata-list'),
    path('stockdata/<int:pk>/', StockDataDetail.as_view(), name='stockdata-detail'),
    path('stockdata/create/', StockDataCreate.as_view(), name='stockdata-create'),

    
    path('symbols/', SymbolList.as_view(), name='symbol-list'),
    path('fetchData/', fetch_data, name='fetch-data'),

    path('calculate-sma/', calculate_sma_view, name='calculate-sma'),





]

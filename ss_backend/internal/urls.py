from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from internal.symbol.views import SymbolList, SymbolViewSet
from internal.stocksdata.views import *
from internal.utility.views import fetch_data
from internal.indicators.views import calculate_sma_view, indicator, maSlopeAnalysis,maConvergence
from internal.watchlists.views import WatchListView,getPublicWatchLists

from internal.watchlistmapping.views import *

router = DefaultRouter()
router.register(r'symbol', SymbolViewSet)


urlpatterns = [
     
     path('', include(router.urls)),
     path('symbols/', SymbolList.as_view(), name='symbol-list'), 

     
     path('stockdata/', StockDataList.as_view(), name='stockdata-list'),
     path('stockdata/<int:pk>/', StockDataDetail.as_view(), name='stockdata-detail'),
     path('stockdata/create/', StockDataCreate.as_view(), name='stockdata-create'),
     path('delete-stock-data/<str:symbol>/',CustomStockDataDelete.as_view(), name='custom-stock-data-delete'),
     path('delete-all-stock-data/', DeleteAllStockData.as_view(),name='delete-all-stock-data'),
     
     path('stockdata/<str:symbol>/', StockDataBySymbol.as_view(),name='stock-data-by-symbol'), 

     
     path('watchlists/', WatchListView.as_view(), name='watchlists'), 

     
     path('fetchData/', fetch_data, name='fetch-data'),     

     
     path('calculate-sma/', calculate_sma_view, name='calculate-sma'),     

     
     # ## Symbol urls
     
     # path('symbol/', include('internal.symbol.urls')),    

     
     # ## StockData urls
     
     # path('stocks-data/', include('internal.stocksdata.urls')),     

     
     # ## WatchList urls
     
     # path('watchlists/', include('internal.watchlists.urls')), 

     
     ## WatchListMapping urls
     
     # path('watchlists-mapping/', include('internal.watchlistsmapping.urls')),
     
     path("public-watchlists/", getPublicWatchLists, name="get_public_watchlists"),
     
     path("indicator/", indicator, name="indicator"),
     
     path("ma-slope-analysis/", maSlopeAnalysis, name="ma_slope_analysis"),
     path("ma-convergence/", maConvergence, name="ma_convergence"),     


]
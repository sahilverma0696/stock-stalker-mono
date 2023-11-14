from django.db import router
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from internal.symbol.views import SymbolList,SymbolViewSet

router = DefaultRouter()
router.register(r'symbol',SymbolViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('', SymbolList.as_view(), name='symbol-list'),
]


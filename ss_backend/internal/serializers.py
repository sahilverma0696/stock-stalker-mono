from rest_framework import serializers
from .models import StockData,Symbol, WatchList

class StockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockData
        fields = '__all__'

class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model= WatchList
        fields ='__all__'
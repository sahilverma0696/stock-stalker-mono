from rest_framework import serializers
from .models import StockData,Symbol,Lists

class StockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockData
        fields = '__all__'

class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = '__all__'

class ListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lists
        fields = '__all__'
from rest_framework import serializers
from internal.watchlistmapping.models import WatchListMapping   


class WatchListMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model= WatchListMapping
        fields ='__all__'
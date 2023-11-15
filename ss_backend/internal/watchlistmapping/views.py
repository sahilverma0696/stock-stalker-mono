from rest_framework.decorators import api_view, authentication_classes,permission_classes
from django.http import JsonResponse
from django.core.serializers import serialize

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from internal.watchlistmapping.models import WatchListMapping
from internal.watchlists.models import WatchList

import json

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([AllowAny, IsAuthenticatedOrReadOnly])
def get_watchlists(request):
    # Get the request parameters.
    list_name = request.query_params.get("list_name")
    user_id = request.query_params.get("user_id")

    # If the list name is specified, return the list of symbols associated with that list.
    if list_name:
        symbols = WatchListMapping.objects.filter(list_name=list_name).values_list("symbol", flat=True)
        return JsonResponse(symbols)

    # If the user ID is specified, return all the watchlists associated with that user.
    elif user_id:
        watchlists = WatchList.objects.filter(user_id=user_id)
        serialized_data = serialize("json", watchlists)
        serialized_data = json.loads(serialized_data)
        return JsonResponse(serialized_data,safe=False, status=200)

    # Otherwise, return all the public watchlists.
    else:
        watchlists = WatchList.objects.filter(is_public=True)
        serialized_data = serialize("json", watchlists)
        serialized_data = json.loads(serialized_data)
        return JsonResponse(serialized_data,safe=False, status=200)

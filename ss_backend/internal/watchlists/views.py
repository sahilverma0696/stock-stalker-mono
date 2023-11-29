from django.http import JsonResponse
from email import message
from rest_framework.response import Response
from rest_framework.views import APIView
from internal.symbol.models import Symbol
from internal.watchlists.models import WatchList
from internal.watchlistmapping.models import WatchListMapping
from rest_framework import permissions, authentication
from users.models import CustomUser
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly


# Class to get the public lists and to make a public or a private list
class WatchListView(APIView):
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication
                              ]
    permission_classes = [
        permissions.AllowAny,
        permissions.IsAuthenticatedOrReadOnly,
    ]

    """
    PROOF
    Provides WatchList by userID 
    - if list_name provided:that list symbols
    - else all lists and symbols under that userID 

    """

    def get(self, request):
        # Get the list name and user ID from the request.
        listName = request.query_params.get("list_name")
        userID = request.user.id

        # Get all the watchlists for the user, if the user ID is specified.
        if listName != None:
            watchlists = WatchList.objects.filter(list_name=listName)
        else:
            watchlists = WatchList.objects.all()

        # Create a list of JSON objects, with each object containing the watchlist name and the list of symbols.
        results = []
        for watchlist in watchlists:
            symbols = WatchListMapping.objects.filter(
                list_name=watchlist, user_id=userID).values_list("symbol", flat=True)
            if symbols:
                results.append({watchlist.list_name: list(symbols)})

        # Return the list of JSON objects in the response.
        if results:
            return Response(results, status=200)
        else:
            return Response(results, status=204)

    """
    PROOF
    Creates public and private watchlist for the user
    Public watchlist, allowed only by staff & superuser
    Private watchlust, allowed by logged in user
    """

    def post(self, request):
        # Validate the request
        watchlist = WatchList()
        watchlist.list_name = request.data.get("list_name")
        is_public = request.data.get("is_public", False)

        # Check if the user is a staff or superuser before making a public list
        if is_public and not (request.user.is_staff or request.user.is_superuser):
            ## Permission denied: Only staff or superusers can create public watchlists.
            return Response("Forbidden Access", status=403)

        watchlist.is_public = is_public
        watchlist.save()

        symbol_list = request.data.get("symbols", [])

        # TODO: save entry in WatchListMapping for each symbol in symbol list
        for symbol in symbol_list:
            watchlistmapping = WatchListMapping()
            watchlistmapping.list_name = watchlist
            watchlistmapping.symbol = Symbol.objects.get(symbol=symbol)
            watchlistmapping.user_id = CustomUser.objects.get(
                id=request.user.id)
            watchlistmapping.save()

        return Response("success", status=201)

    # TODO: 1. Make DEL, UPDATE




"""
PROOF
Provides paginated all public WatchLists
"""
# TODO: Add pagination


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([AllowAny, IsAuthenticatedOrReadOnly])
def getPublicWatchLists(request):
    listName = request.query_params.get("list_names")

    results = []
    if not listName:
        # send all public watchlists
        publicLists = WatchList.objects.filter(is_public=True)
        for eachList in publicLists:
            symbols = WatchListMapping.objects.filter(list_name=eachList)
            if symbols:
                symbolList = []
                for eachSymbol in symbols:
                    symbolList.append(eachSymbol.symbol.symbol)
                results.append({eachList.list_name: symbolList})

    else:
        publicList = WatchList.objects.filter(
            is_public=True, list_name=listName)
        for eachList in publicList:
            symbols = WatchListMapping.objects.filter(list_name=eachList)
            if symbols:
                for eachSymbol in symbols:
                    results.append({eachList.list_name: eachSymbol.symbol})

    if results:
        return Response(results, status=200)
    else:
        return Response([], status=204)

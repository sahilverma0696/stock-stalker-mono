from rest_framework.response import Response
from rest_framework.views import APIView
from internal.symbol.models import Symbol
from internal.watchlists.models import WatchList
from internal.watchlistmapping.models import WatchListMapping
from rest_framework import permissions, authentication
from users.models import CustomUser


## Class to get the public lists and to make a public or a private list
class WatchListView(APIView):
    authentication_classes =[authentication.SessionAuthentication,
                              authentication.TokenAuthentication
                            ]
    permission_classes =[
                            permissions.AllowAny,
                            permissions.IsAuthenticatedOrReadOnly,
                        ]

    def get(self, request):
        # Get the list name and user ID from the request.
        list_name = request.query_params.get("list_name")
        user_id = request.query_params.get("user_id")

        # Get all the watchlists for the user, if the user ID is specified.
        watchlists = WatchList.objects.all()

        # Create a list of JSON objects, with each object containing the watchlist name and the list of symbols.
        results = []
        for watchlist in watchlists:
            symbols = WatchListMapping.objects.filter(
                list_name=watchlist).values_list("symbol", flat=True)
            results.append({watchlist.list_name: list(symbols)})

        # Return the list of JSON objects in the response.
        return Response(results)

    def post(self, request):
        # Validate the request
        watchlist = WatchList()
        watchlist.list_name = request.data.get("list_name")
        is_public = request.data.get("is_public", False)
    
        # Check if the user is a staff or superuser before making a public list
        if not request.user.is_staff and not request.user.is_superuser and is_public:
            return Response("Permission denied: Only staff or superusers can create public watchlists.", status=403)
    
        watchlist.is_public = is_public
        watchlist.save()
    
        symbol_list = request.data.get("symbols", [])
    
        # TODO: save entry in WatchListMapping for each symbol in symbol list
        for symbol in symbol_list:
            watchlistmapping = WatchListMapping()
            watchlistmapping.list_name = watchlist
            watchlistmapping.symbol = Symbol.objects.get(symbol=symbol)
            watchlistmapping.user_id = CustomUser.objects.get(id=request.user.id)
            watchlistmapping.save()
    
        return Response("success")


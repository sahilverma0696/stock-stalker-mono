from django.db import models
from internal.watchlists.models import WatchList
from internal.symbol.models import Symbol
from users.models import CustomUser

class WatchListMapping(models.Model):
    list_name = models.ForeignKey(WatchList,to_field='id',on_delete=models.CASCADE)
    symbol = models.ForeignKey(Symbol, to_field='symbol',on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True) # TODO: Handle this field properly

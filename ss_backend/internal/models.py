from django.db import models
from users.models import CustomUser
from django.db.models import Max
from django.db.models import Q




## Symbol Table
class Symbol(models.Model):
    symbol = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.symbol

    @classmethod
    def get_all_symbols(cls):
        #all_symbols = Symbol.get_all_symbols()
        return list(cls.objects.values_list('symbol', flat=True))

## Historical Data
class StockData(models.Model):
    date = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    symbol = models.ForeignKey(Symbol, to_field='symbol',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.symbol}"
    
    @classmethod
    def get_latest_date(cls, stock_id):
        try:
            latest_date = cls.objects.filter(symbol=stock_id).aggregate(Max('date'))['date__max']
            return latest_date
        except cls.DoesNotExist:
            return None

## Lists Table
class WatchList(models.Model):
    list_name = models.CharField(max_length=50)
    is_public = models.BooleanField(default=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["list_name"], condition=Q(is_public=True), name="unique_public_list_name"),
        ]



class WatchListMapping(models.Model):
    list_name = models.ForeignKey(WatchList,to_field='id',on_delete=models.CASCADE)
    symbol = models.ForeignKey(Symbol, to_field='symbol',on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True) # TODO: Handle this field properly

from django.db import models
from users.models import CustomUser
from django.db.models import Max
from django.db.models import Q
from django.utils import timezone
import datetime
import pytz
from django.conf import settings



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

    class Meta:
        unique_together = ['date', 'symbol']

    def __str__(self):
        return f"{self.date} - {self.symbol}"
    
    def get_latest_date_from_db(symbol, time_zone=settings.TIME_ZONE):
        """
        Get the latest date from the db for a symbol.

        Args:
            symbol (str): The symbol of the stock to get the latest date for.
            time_zone (str): The time zone to adjust the latest date to.

        Returns:
            datetime.datetime: The latest date for the given symbol.
        """

        # Get the latest date from the db.
        latest_date = StockData.objects.filter(symbol=symbol).aggregate(Max('date'))['date__max']

        # If the latest date is not None, adjust it to the given time zone.
        if latest_date is not None:
            latest_date = latest_date.astimezone(pytz.timezone(time_zone))

        # Return the latest date.
        return latest_date

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

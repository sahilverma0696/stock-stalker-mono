from django.db import models
from datetime import timedelta
import pandas as pd
import talib
import logging


logger = logging.getLogger(__name__)


## Historical stock data table
class StockData(models.Model):
    date = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    symbol = models.CharField(max_length=255)

    class Meta:
        unique_together = ('date', 'symbol')

    def __str__(self):
        return f"{self.date} - {self.symbol}"



#---------------------

## Symbol Table
class Symbol(models.Model):
    symbol = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.symbol

    @classmethod
    def get_all_symbols(cls):
        #all_symbols = Symbol.get_all_symbols()
        return list(cls.objects.values_list('symbol', flat=True))

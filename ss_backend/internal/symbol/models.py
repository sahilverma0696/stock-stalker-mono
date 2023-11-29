from django.db import models


## Symbol Table
class Symbol(models.Model):
    symbol = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.symbol

    @classmethod
    def get_all_symbols(cls):
        #all_symbols = Symbol.get_all_symbols()
        return list(cls.objects.values_list('symbol', flat=True))
from django.db import models
from users.models import CustomUser
from django.contrib.postgres.fields import ArrayField


## Symbol Table
class Symbol(models.Model):
    symbol_id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.symbol

    @classmethod
    def get_all_symbols(cls):
        #all_symbols = Symbol.get_all_symbols()
        return list(cls.objects.values_list('symbol', flat=True))
    @classmethod
    def get_symbol_id_and_symbol(cls):
        symbol_data = list(cls.objects.values_list('symbol_id', 'symbol'))
        return [(symbol_id, symbol) for symbol_id, symbol in symbol_data]

## Historical Data
class StockData(models.Model):
    stock_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    symbol = models.ForeignKey(Symbol, to_field='symbol',on_delete=models.CASCADE)  # Use symbol_id as a foreign key


    def __str__(self):
        return f"{self.date} - {self.symbol}"

## Lists Table
class Lists(models.Model):
    list_id   = models.AutoField(primary_key=True)
    list_name = models.CharField(max_length=50)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    is_public = models.BooleanField(default=True)
    symbols = ArrayField(models.CharField(max_length=100), blank=True)

    def __str__(self):
        return self.list_name

class UserListMapping(models.Model):
    user_list_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    list_id = models.ForeignKey(Lists, on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.user.user_id} - List {self.list_id.list_id}"
from django.db import models
from internal.symbol.models import Symbol
from django.conf import settings
from django.db.models import Max
from pytz import timezone as pytzTimezone
from django.utils import timezone
from datetime import timedelta



## Historical Data
class StockData(models.Model):
    date = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    symbol = models.ForeignKey(Symbol, to_field='symbol',on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Ensure the datetime is timezone-aware before saving
        if not self.date.tzinfo:
            self.date = timezone.make_aware(self.date)

        super().save(*args, **kwargs)

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
            latest_date = latest_date.astimezone(pytzTimezone(time_zone))

        # Return the latest date.
        return latest_date
from datetime import timedelta,datetime
from internal.stocksdata.models import StockData

def is_time_difference_valid(prev_date, today_date, max_business_days=2):
    # Define the list of weekend days (0 = Monday, 6 = Sunday)
    weekend_days = [5, 6]  # Saturday and Sunday

    # Initialize a counter for business days
    business_days = 0

    # Calculate the difference between dates
    delta = today_date - prev_date

    # Loop through the days in the date range
    for i in range(delta.days + 1):
        current_date = prev_date + timedelta(days=i)
        if current_date.weekday() not in weekend_days:
            business_days += 1

    # Check if the number of business days difference is greater than or equal to the specified maximum
    return business_days >= max_business_days

# Create your views here.
def getDate(pSymbol):
    """Returns the last recent data from which data needed to be fetched"""
    ## YYYY-MM-DD    
    latest_date = datetime(2015, 1, 1)
   
    # Check if data for "SBIN" exists in the model
    if StockData.objects.filter(symbol=pSymbol).exists():
        latest_date = StockData.get_latest_date_from_db(pSymbol)
    
    return latest_date


from datetime import datetime, timedelta

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
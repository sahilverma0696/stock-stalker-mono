import time
import random
import logging
import pytz
import yfinance as yf 
import pandas as pd 
from internal.models import StockData,Symbol
from internal.views import getDate

from collections import Counter
from django.db import IntegrityError


logger = logging.getLogger(__name__)

#TODO: Make this function fucking clean and powerful
#TODO: resume data fetch for the symbols for which fetch failed
#TODO: Potential Break in type ignore for date type
# Return a type to this function
def fetchData(pDate=None):
    logger.info("Starting data fetch")

    symbol_id_and_symbol_list = Symbol.get_symbol_id_and_symbol()
    if not symbol_id_and_symbol_list:
        logger.error("Symbol list is empty")

    logger.info(symbol_id_and_symbol_list)
    if pDate is None:
        date = getDate()
    else:
        date = pDate
    logger.info("Starting date as date %s", date)

    fetchedData = []
    try:
        for symbol_id, each_symbol in symbol_id_and_symbol_list:
            logger.info("Fetching data for %s", each_symbol)
            df = yf.Ticker(f'{each_symbol}.NS').history(start=date)
            
            for index, row in df.iterrows():
                stock_data = StockData()
                stock_data.date = index # type: ignore
                stock_data.open = row['Open']
                stock_data.high = row['High']
                stock_data.low = row['Low']
                stock_data.close = row['Close']
                stock_data.volume = row['Volume']
                
                try:
                    # Attempt to save the stock_data
                    symbol_instance = Symbol.objects.get(symbol=each_symbol)
                    stock_data.symbol = symbol_instance
                    stock_data.save()
                except IntegrityError:
                    # Handle the case where the entry is already in the database
                    logger.warning("Duplicate entry for symbol %s on date %s", each_symbol, index)

            fetchedData.append(each_symbol)
            delay_seconds = random.randint(4, 7)
            logger.info("Waiting for %d seconds before the next symbol...", delay_seconds)
            time.sleep(delay_seconds)
    except Exception as e:
        logger.error("An error occurred while fetching and saving data: %s", e)

    if Counter(fetchedData) == Counter([symbol for _, symbol in symbol_id_and_symbol_list]):
        logger.info("Data fetched for all symbols")
    else:
        logger.info("Data NOT fetched for all symbols")

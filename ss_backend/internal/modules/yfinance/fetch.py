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
import datetime


logger = logging.getLogger(__name__)

#TODO: Make this function fucking clean and powerful
#TODO: resume data fetch for the symbols for which fetch failed
#TODO: Potential Break in type ignore for date type
#TODO: start fetch from lastest_date+1
# Return a type to this function
def fetchData(pDate=None):
    logger.info("Starting data fetch")

    symbol_list = Symbol.get_all_symbols()
    if not symbol_list:
        logger.error("Symbol list is empty")

    logger.info(symbol_list)

    fetchedData = []
    try:
        for each_symbol in symbol_list:
            iDate = getDate(each_symbol)
            logger.info("Latest date from db %s, vs present date %s",iDate,datetime.date.today())
            if iDate == datetime.date.today():
                logger.info("Upto-date data present for %s to date %s, skipping for same", each_symbol, iDate)
                continue

            logger.info("Fetching data for %s from the date %s", each_symbol,iDate)
            df = yf.Ticker(f'{each_symbol}.NS').history(start=iDate)
            
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
                    stock_data.symbol = Symbol.objects.get(symbol=each_symbol)
                    stock_data.save()
                except IntegrityError:
                    # Handle the case where the entry is already in the database
                    logger.warning("Duplicate entry for symbol %s on date %s", each_symbol, index)

            fetchedData.append(each_symbol)
            delay_seconds = 1
            logger.info("Waiting for %d seconds before the next symbol...", delay_seconds)
            time.sleep(delay_seconds)
    except Exception as e:
        logger.error("An error occurred while fetching and saving data: %s", e)

    if Counter(fetchedData) == Counter([symbol for symbol in symbol_list]):
        logger.info("Data fetched for all symbols")
    else:
        logger.info("Data NOT fetched for all symbols")

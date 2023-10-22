import time
import random
import logging
import os
import yfinance as yf 
import pandas as pd 
from internal.models import StockData,Symbol
from internal.views import getDate


logger = logging.getLogger(__name__)


def fetchData():
    logger.info("Starting data fetch")
    symbolList = Symbol.get_all_symbols()
    date = getDate()
    try:
        for each_symbol in symbolList:
            logger.info("Fetching data for %s", each_symbol)
            df = yf.Ticker(f'{each_symbol}.NS').history(start=date)
            for index, row in df.iterrows():
                stock_data = StockData()
                stock_data.date = index
                stock_data.open = row['Open']
                stock_data.high = row['High']
                stock_data.low = row['Low']
                stock_data.close = row['Close']
                stock_data.volume = row['Volume']
                stock_data.symbol = each_symbol
                stock_data.save()
                
            # Introduce a random delay between 5 to 10 seconds
            delay_seconds = random.randint(5, 10)
            logger.info("Waiting for %d seconds before the next symbol...", delay_seconds)
            time.sleep(delay_seconds)
    except Exception as e:
        logger.error("An error occurred while fetching and saving data: %s", e)

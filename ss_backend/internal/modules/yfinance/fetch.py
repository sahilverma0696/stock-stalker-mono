import time
import random
import logging
import os
import yfinance as yf 
import pandas as pd 
from internal.models import StockData,Symbol
from internal.views import getDate

from collections import Counter


logger = logging.getLogger(__name__)

#TODO: resume data fetch for the symbols for which fetch failed
def fetchData(pDate=None):
    logger.info("Starting data fetch")

    symbolList = Symbol.get_all_symbols()
    if symbolList == None:
        logger.error("symbol list empty")

    if pDate is None:
        date = getDate()
    else:
        date = pDate
    logger.info(" starting date as date %s",date)

    fetchedData = []
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
                try:
                    # Attempt to save the stock_data
                    stock_data.save()
                except IntegrityError:
                    #Handle the case where the entry is already in the database
                    logger.warning("Duplicate entry for symbol %s on date %s", each_symbol, index)
                
            
            fetchedData.append(each_symbol)
            delay_seconds = random.randint(4, 7)
            logger.info("Waiting for %d seconds before the next symbol...", delay_seconds)
            time.sleep(delay_seconds)
    except Exception as e:
        logger.error("An error occurred while fetching and saving data: %s", e)
    
    if Counter(fetchedData) == Counter(symbolList):
        logger.log("Data fetched for all symbols")
    else:
        logger.log("Data NOT fetched for all symbols")

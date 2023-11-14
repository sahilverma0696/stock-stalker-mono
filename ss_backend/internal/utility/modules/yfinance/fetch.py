import time
from stock_stalker.basic import LOG
import yfinance as yf
from internal.stocksdata.models import StockData
from internal.symbol.models import Symbol
from internal.utility.modules.dateutility.datefunc import getDate

from collections import Counter
from django.db import IntegrityError
import datetime


# TODO: Make this function fucking clean and powerful
# TODO: resume data fetch for the symbols for which fetch failed
# TODO: Potential Break in type ignore for date type
# TODO: start fetch from lastest_date+1
# Return a type to this function
def fetchData(pDate=None):
    LOG.info("Starting data fetch")

    symbol_list = Symbol.get_all_symbols()
    if not symbol_list:
        LOG.error("Symbol list is empty")

    LOG.info(symbol_list)

    fetchedData = []
    try:
        for each_symbol in symbol_list:
            iDate = getDate(each_symbol)
            LOG.info("Latest date from db %s, vs present date %s",
                     iDate, datetime.date.today())
            if iDate == datetime.date.today():
                LOG.info(
                    "Upto-date data present for %s to date %s, skipping for same", each_symbol, iDate)
                continue

            LOG.info("Fetching data for %s from the date %s",
                     each_symbol, iDate)
            df = yf.Ticker(f'{each_symbol}.NS').history(start=iDate)

            for index, row in df.iterrows():
                stock_data = StockData()
                stock_data.date = index  # type: ignore
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
                    LOG.warning(
                        "Duplicate entry for symbol %s on date %s", each_symbol, index)

            fetchedData.append(each_symbol)
            delay_seconds = 1
            LOG.info(
                "Waiting for %d seconds before the next symbol...", delay_seconds)
            time.sleep(delay_seconds)
    except Exception as e:
        LOG.error("An error occurred while fetching and saving data: %s", e)

    if Counter(fetchedData) == Counter([symbol for symbol in symbol_list]):
        LOG.info("Data fetched for all symbols")
    else:
        LOG.info("Data NOT fetched for all symbols")

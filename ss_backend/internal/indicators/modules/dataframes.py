from internal.stocksdata.models import StockData
import pandas as pd


def getDataFrame(symbol, num_days):
    # Get historical data from the database
    historical_data = StockData.objects.filter(
        symbol=symbol).order_by('-date')[:num_days]

    df = pd.DataFrame.from_records(historical_data.values())
    # Set the 'date' column as the index
    df.set_index('date', inplace=True)

    # Convert the 'date' index to datetime format and discard the time component
    df.index = pd.to_datetime(df.index).date  # type: ignore

    df.index.set_names(['date'], inplace=True)  # type: ignore
    # Drop the 'id' column
    df.drop('id', axis=1, inplace=True)
    return df


def getDataFrameMap(pSymbols: list, pDays: int):
    uMap = dict()
    for eachSymbol in pSymbols:
        uMap[eachSymbol] = getDataFrame(eachSymbol, pDays)
    return uMap

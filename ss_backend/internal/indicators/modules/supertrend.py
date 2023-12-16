import pandas_ta as ta 

def supertrend_with_pandas_ta(df, period=10, multiplier=3, ohlc=["Open", "High", "Low", "Close"]):

    """
    Calculates the Supertrend indicator for a DataFrame using pandas_ta.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        period (int): Period for Average True Range (ATR) calculation (default: 10).
        multiplier (int): Multiplier for ATR in Supertrend formula (default: 3).
        ohlc (list): List of column names for Open, High, Low, and Close (default: ["Open", "High", "Low", "Close"]).

    Returns:
        pandas.DataFrame: The original DataFrame with additional columns for Supertrend and Supertrend direction.
    """

    indicator = ta.supertrend(high=df[ohlc[1]], low=df[ohlc[2]], close=df[ohlc[3]], period=period, multiplier=multiplier,append=True)

    return df
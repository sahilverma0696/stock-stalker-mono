import pandas as pd

"""
Provides SMA, in this case pDays is the window size, the number of days
SMA_diff for latest is NaN cause it depends on coming date 
SMA_diff = SMA_current - SMA_previous
so that's an expected behaviour to be handled,accordingly
"""
def simpleMovingAverage(df,pDays):
    # Calculate the SMA
    df['SMA'] = df['close'].rolling(window=pDays).mean()

    # Calculate the difference between consecutive SMA values
    df['SMA_diff'] = df['SMA'].diff()

    # Identify trends
    df['SMA_trend'] = df['SMA_diff'] > 0

    ## TODO: moving this to upper application layer

    # Calculate the proportion of True values in SMA_trend
    # proportion_increasing = df['SMA_trend'].iloc[:-1].mean()

    # # Set SMA_trend_direction
    # if proportion_increasing > 0.5:
    #     df['SMA_trend_direction'] = 'Increasing'
    # elif proportion_increasing == 0.5:
    #     df['SMA_trend_direction'] = 'Neutral'
    # else:
    #     df['SMA_trend_direction'] = 'Decreasing'



def exponentialMovingAverage(df, pDays):
    # Calculate the EMA
    df['EMA'] = df['close'].ewm(span=pDays, min_periods=pDays - 1).mean()

    # Calculate the difference between consecutive EMA values
    df['EMA_diff'] = df['EMA'].diff()

    # Identify trends
    df['EMA_trend'] = df['EMA_diff'] > 0

    ## TODO: moving this to upper application layer
    # Calculate the proportion of True values in EMA_trend
    # proportion_increasing = df['EMA_trend'].iloc[:-1].mean()

    # # Set EMA_trend_direction
    # if proportion_increasing > 0.5:
    #     df['EMA_trend_direction'] = 'Increasing'
    # elif proportion_increasing == 0.5:
    #     df['EMA_trend_direction'] = 'Neutral'
    # else:
    #     df['EMA_trend_direction'] = 'Decreasing'

    # # Calculate EMA_trend_min, EMA_trend_max, EMA_trend_exact_pDays2
    # df['EMA_trend_min'] = df['EMA_trend'].rolling(window=pDays2).min()
    # df['EMA_trend_max'] = df['EMA_trend'].rolling(window=pDays2).max()
    # df['EMA_trend_exact_pDays2'] = df['EMA_trend'].rolling(window=pDays2).apply(lambda x: x.all())

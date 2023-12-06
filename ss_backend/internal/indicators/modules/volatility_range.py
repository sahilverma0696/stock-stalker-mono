import pandas_ta as ta

def append_atr(df, column="Close", high="High", low="Low", length=14, offset=0, suffix="_ATR", inplace=True):

    """
    Calculates and appends the Average True Range (ATR) to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the ATR will be calculated.
        column (str): Name of the column to use for closing prices (default: "Close").
        high (str): Name of the column to use for high prices (default: "High").
        low (str): Name of the column to use for low prices (default: "Low").
        length (int): Number of periods for the ATR calculation (default: 14).
        offset (int): Number of periods to shift the ATR forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new ATR column name (default: "_ATR").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the ATR appended as a new column (in-place modification).
    """

    if not inplace:
        raise ValueError("The `append_atr` function only supports in-place modification (inplace=True).")

    # Calculate the ATR and append it to the DataFrame
    df.ta.atr(high=high, low=low, close=column, length=length, offset=offset,append=True)

    return df

def append_donchian_channel(df, column="Close", period=20, offset=0, suffix="_DC", inplace=True):

    """
    Calculates and appends the Donchian Channel (upper and lower bands) to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the Donchian Channel will be calculated.
        column (str): Name of the column to use for calculating the Donchian Channel (default: "Close").
        period (int): Number of periods for the Donchian Channel calculation (default: 20).
        offset (int): Number of periods to shift the Donchian Channel forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new Donchian Channel column names (default: "_DC").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the Donchian Channel upper and lower bands appended as new columns (in-place modification).
    """

    if not inplace:
        raise ValueError("The `append_donchian_channel` function only supports in-place modification (inplace=True).")

    df.ta.donchian(high=column, close=column, low=column, period=period, offset=offset,append=True)


import pandas_ta as ta

def append_keltner_channel(df, column="Close", period=14, multiplier=2.0, offset=0, suffix="_KC", inplace=True):

    """
    Calculates and appends the Keltner Channel (KC) upper and lower bands to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the Keltner Channel will be calculated.
        column (str): Name of the column to use for calculating the Keltner Channel (default: "Close").
        period (int): Number of periods for the Keltner Channel calculation (default: 14).
        multiplier (float): Multiplier for the Average True Range (ATR) to determine the channel width (default: 2.0).
        offset (int): Number of periods to shift the Keltner Channel forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new Keltner Channel column names (default: "_KC").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the Keltner Channel upper and lower bands appended as new columns (in-place modification).
    """

    if not inplace:
        raise ValueError("The `append_keltner_channel` function only supports in-place modification (inplace=True).")

    # Calculate the EMA and ATR
    ema = df.ta.ema(close=column, length=period, offset=offset)
    atr = df.ta.atr(high=column, low=column, close=column, length=period, offset=offset)

    # Calculate the upper and lower Keltner Channel bands
    upper_band = ema + multiplier * atr
    lower_band = ema - multiplier * atr

    # Add the Upper and Lower Keltner Channel bands as new columns to the DataFrame
    df[f"{column}{suffix}_upper"] = upper_band
    df[f"{column}{suffix}_lower"] = lower_band

    return df



def append_volatility_ratio_tr(df, column="Close", high="High", low="Low", period=14, offset=0, suffix="_VR_TR", inplace=True):

    """
    Calculates and appends the Volatility Ratio (VR) using True Range (TR) to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the VR will be calculated.
        column (str): Name of the column to use for closing prices (default: "Close").
        high (str): Name of the column to use for high prices (default: "High").
        low (str): Name of the column to use for low prices (default: "Low").
        period (int): Number of periods for the ATR calculation (default: 14).
        offset (int): Number of periods to shift the VR forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new VR column name (default: "_VR_TR").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the VR appended as a new column (in-place modification).
    """

    if not inplace:
        raise ValueError("The `append_volatility_ratio_tr` function only supports in-place modification (inplace=True).")

    # Calculate the True Range (TR)
    tr = df[high] - df[low]
    tr = abs(tr)

    # Calculate the Average True Range (ATR)
    atr = df.ta.atr(high=high, low=low, close=column, length=period, offset=offset)

    # Calculate the VR
    vr = tr / atr

    # Add the VR as a new column to the DataFrame
    df[f"{column}{suffix}"] = vr

    return df


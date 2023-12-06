def append_obv(df, column="Close", volume_column="Volume", offset=0, suffix="_OBV", inplace=True):

    """
    Calculates and appends the On-Balance Volume (OBV) to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the OBV will be calculated.
        column (str): Name of the column to use for the volume direction (default: "Close").
        volume_column (str): Name of the volume column (default: "Volume").
        offset (int): Number of periods to shift the OBV forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new OBV column name (default: "_OBV").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the OBV appended as a new column (in-place modification).
    """

    if not inplace:
        raise ValueError("The `append_obv` function only supports in-place modification (inplace=True).")

    # Calculate the OBV and append it to the DataFrame
    df.ta.obv(close=column, volume=volume_column, offset=offset,append=True)



def append_mfi(df, column="Close", high="High", low="Low", volume="Volume", length=14, offset=0, suffix="_MFI", inplace=True):

    """
    Calculates and appends the Money Flow Index (MFI) to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the MFI will be calculated.
        column (str): Name of the column to use for closing prices (default: "Close").
        high (str): Name of the column to use for high prices (default: "High").
        low (str): Name of the column to use for low prices (default: "Low").
        volume (str): Name of the column to use for volume data (default: "Volume").
        length (int): Number of periods for the MFI calculation (default: 14).
        offset (int): Number of periods to shift the MFI forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new MFI column name (default: "_MFI").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the MFI appended as a new column (in-place modification).
    """

    if not inplace:
        raise ValueError("The `append_mfi` function only supports in-place modification (inplace=True).")

    # Calculate the MFI and append it to the DataFrame
    df.ta.mfi(high=high, low=low, close=column, volume=volume, length=length, offset=offset,append=True)
    

    return df


import pandas_ta as ta


def append_ad(df, column="Close", high="High", low="Low", volume="Volume", offset=0, suffix="_AD", inplace=True):

    """
    Calculates and appends the Accumulation/Distribution Indicator (A/D) to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the A/D will be calculated.
        column (str): Name of the column to use for closing prices (default: "Close").
        high (str): Name of the column to use for high prices (default: "High").
        low (str): Name of the column to use for low prices (default: "Low").
        volume (str): Name of the column to use for volume data (default: "Volume").
        offset (int): Number of periods to shift the A/D forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new A/D column name (default: "_AD").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the A/D appended as a new column (in-place modification).
    """

    if not inplace:
        raise ValueError("The `append_ad` function only supports in-place modification (inplace=True).")

    # Calculate the A/D and append it to the DataFrame
    df.ta.ad(high=high, low=low, close=column, volume=volume, offset=offset,append=True)

    return df

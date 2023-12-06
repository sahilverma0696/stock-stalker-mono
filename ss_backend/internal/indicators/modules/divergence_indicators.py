def append_rsi(df, column="Close", length=14, offset=0, suffix="_RSI", inplace=True):

    """
    Calculates and appends the Relative Strength Index (RSI) to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the RSI will be calculated.
        column (str): Name of the column to use for calculating the RSI (default: "Close").
        length (int): Number of periods for the RSI calculation (default: 14).
        offset (int): Number of periods to shift the RSI forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new RSI column name (default: "_RSI").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the RSI appended as a new column (in-place modification).
    """

    if not inplace:
        raise ValueError("The `append_rsi` function only supports in-place modification (inplace=True).")

    # Calculate the RSI and append it to the DataFrame
    df.ta.rsi(close=column, length=length, offset=offset,append=True)

def append_cci(df, column="Close", mean_period=14, deviation_period=7, offset=0, suffix="_CCI", inplace=True):

    """
    Calculates and appends the Commodity Channel Index (CCI) to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the CCI will be calculated.
        column (str): Name of the column to use for calculating the CCI (default: "Close").
        mean_period (int): Number of periods for the mean calculation (default: 14).
        deviation_period (int): Number of periods for the standard deviation calculation (default: 7).
        offset (int): Number of periods to shift the CCI forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new CCI column name (default: "_CCI").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the CCI appended as a new column (in-place modification).
    """

    if not inplace:
        raise ValueError("The `append_cci` function only supports in-place modification (inplace=True).")

    # Calculate the CCI and append it to the DataFrame
    df.ta.cci(high=column, low=column, close=column, mean_period=mean_period, deviation_period=deviation_period, offset=offset,append=True)


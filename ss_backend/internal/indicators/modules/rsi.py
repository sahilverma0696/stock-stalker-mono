import pandas_ta as ta

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

    return df

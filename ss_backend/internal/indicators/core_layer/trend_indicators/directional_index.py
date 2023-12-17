import pandas_ta as ta

def append_adx(df, column="Close", length=14, offset=0, suffix="_ADX", inplace=True):

    """
    Calculates and appends the Average Directional Index (ADX) to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the ADX will be calculated.
        column (str): Name of the column to use for calculating the ADX (default: "Close").
        length (int): Number of periods for the ADX calculation (default: 14).
        offset (int): Number of periods to shift the ADX forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new ADX column name (default: "_ADX").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the ADX appended as a new column (in-place modification).
    """

    if not inplace:
        raise ValueError("The `append_adx` function only supports in-place modification (inplace=True).")

    # Calculate the ADX and append it to the DataFrame
    df.ta.adx(high=column, low=column, close=column, length=length, offset=offset,append=True)

    return df
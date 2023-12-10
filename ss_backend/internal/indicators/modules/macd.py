def append_macd(df, column="Close", fast_length=12, slow_length=26, signal_length=9, offset=0, suffix="_MACD", inplace=True):

    """
    Calculates and appends the Moving Average Convergence Divergence (MACD) to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the MACD will be calculated.
        column (str): Name of the column to use for calculating the MACD (default: "Close").
        fast_length (int): Number of periods for the fast EMA (default: 12).
        slow_length (int): Number of periods for the slow EMA (default: 26).
        signal_length (int): Number of periods for the MACD signal line (default: 9).
        offset (int): Number of periods to shift the MACD forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new MACD column names (default: "_MACD").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the MACD appended as new columns (in-place modification).
    """

    if not inplace:
        raise ValueError("The `append_macd` function only supports in-place modification (inplace=True).")

    # Calculate the MACD components and the MACD signal line
    macd = df.ta.macd(close=column, fast_length=fast_length, slow_length=slow_length, signal_length=signal_length, offset=offset,append=True)
    
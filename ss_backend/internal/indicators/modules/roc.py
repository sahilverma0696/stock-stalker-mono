def append_roc(df, column="Close", period=1, offset=0, suffix="_ROC", inplace=True):

    """
    Calculates and appends the Rate of Change (ROC) to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the ROC will be calculated.
        column (str): Name of the column to use for calculating the ROC (default: "Close").
        period (int): Number of periods for the ROC calculation (default: 1).
        offset (int): Number of periods to shift the ROC forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new ROC column name (default: "_ROC").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the ROC appended as a new column (in-place modification).
    """

    if not inplace:
        raise ValueError("The `append_roc` function only supports in-place modification (inplace=True).")

    # Calculate the ROC and append it to the DataFrame
    df.ta.roc(close=column, period=period, offset=offset,append=True)
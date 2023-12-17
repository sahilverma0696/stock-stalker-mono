import pandas_ta as ta 

import pandas_ta as ta

def append_parabolic_sar(df, column="Close", af0=0.02, af=0.2, max_af=0.2, offset=0, suffix="_PSAR", inplace=False):

    """
    Calculates and appends the Parabolic SAR to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the Parabolic SAR will be calculated.
        column (str): Name of the column to use for calculating the Parabolic SAR (default: "Close").
        af0 (float): Initial acceleration factor (default: 0.02).
        af (float): Acceleration factor increment (default: 0.2).
        max_af (float): Maximum acceleration factor (default: 0.2).
        offset (int): Number of periods to shift the Parabolic SAR forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new Parabolic SAR column name (default: "_PSAR").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: False).

    Returns:
        pandas.DataFrame: A DataFrame with the Parabolic SAR appended as a new column.

    Raises:
        ValueError: If an invalid af0, af, or max_af value is provided.
    """

    if af0 <= 0 or af0 > 1:
        raise ValueError("Initial acceleration factor (af0) must be between 0 and 1.")

    if af <= 0 or af > 1:
        raise ValueError("Acceleration factor increment (af) must be between 0 and 1.")

    if max_af <= 0 or max_af > 1:
        raise ValueError("Maximum acceleration factor (max_af) must be between 0 and 1.")

    psar_name = f"{column}{suffix}"
    if not inplace:
        df = df.copy()

    df[psar_name] = df.ta.psar(high=column, low=column, close=column, af0=af0, af=af, max_af=max_af, offset=offset,append=True)

    return df

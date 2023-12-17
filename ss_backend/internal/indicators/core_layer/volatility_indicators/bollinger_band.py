import pandas_ta as ta
import pandas as pd
def append_bollinger_bands(df, column="close", length=20, std_dev=2, offset=0, suffix="_BB"):
    """
    Calculates and appends Bollinger Bands to a DataFrame.

    Args:
        df: The DataFrame where the Bollinger Bands will be calculated.
        column: Name of the column to use for calculating the Bollinger Bands (default: "Close").
        length: Number of periods for the Bollinger Bands calculation (default: 20).
        std_dev: Number of standard deviations to use for the upper and lower bands (default: 2).
        offset: Number of periods to shift the Bollinger Bands forward (positive) or backward (negative) (default: 0).
        suffix: Suffix to add to the new Bollinger Bands column names (default: "_BB").
        inplace: Whether to modify the original DataFrame or return a new one (default: False).

    Returns:
        A DataFrame with the Bollinger Bands appended as new columns.

    Raises:
        ValueError: If an invalid std_dev or offset is provided.
    """

    if std_dev <= 0:
        raise ValueError("Standard deviation for Bollinger Bands must be positive.")

    if offset < 0:
        raise ValueError("Offset for Bollinger Bands cannot be negative.")

    df.ta.bbands(close=column, length=length, std_dev=std_dev, offset=offset,append=True)

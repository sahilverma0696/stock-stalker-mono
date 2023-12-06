import pandas as pd
import pandas_ta as ta

def append_sma(df, column="close", length=44, offset=0, suffix="_SMA", inplace=True):
  """
  Calculates and appends the Simple Moving Average (SMA) to a DataFrame.

  Args:
      df: The DataFrame where the SMA will be calculated.
      column: Name of the column to use for calculating the SMA (default: "Close").
      length: Number of periods for the SMA calculation (default: 20).
      offset: Number of periods to shift the SMA forward (positive) or backward (negative) (default: 0).
      suffix: Suffix to add to the new SMA column name (default: "_SMA").
      inplace: Whether to modify the original DataFrame or return a new one (default: False).

  Returns:
      A DataFrame with the SMA appended as a new column.

  Raises:
      ValueError: If an invalid offset is provided.
  """

  if offset < 0:
      raise ValueError("Offset for SMA cannot be negative.")

  sma_name = f"{column}{suffix}"
  if not inplace:
      df = df.copy()

  df[sma_name] = df.ta.sma(close=column, length=length, offset=offset)

  return df



def append_ema(df, column="close", length=44, smoothing="exponential", offset=0, suffix="_EMA", inplace=True):
  """
  Calculates and appends the Exponential Moving Average (EMA) to a DataFrame.

  Args:
      df: The DataFrame where the EMA will be calculated.
      column: Name of the column to use for calculating the EMA (default: "Close").
      length: Number of periods for the EMA calculation (default: 20).
      smoothing: Averaging method, either "linear" or "exponential" (default: "exponential").
      offset: Number of periods to shift the EMA forward (positive) or backward (negative) (default: 0).
      suffix: Suffix to add to the new EMA column name (default: "_EMA").
      inplace: Whether to modify the original DataFrame or return a new one (default: False).

        Offset	    Interpretation	                                Use cases
        Positive	More responsive, captures recent changes	    Short-term trends, catching up to volatile prices
        Negative	Smoother, filters out noise	                    Long-term trends, ignoring short-term fluctuations
        Zero	    Balanced view, captures both short & long-term	Default, suitable for general analysis

  Returns:
      A DataFrame with the EMA appended as a new column.

  Raises:
      ValueError: If an invalid smoothing method is provided.
  """

  if smoothing not in ("linear", "exponential"):
      raise ValueError("Invalid smoothing method. Choose 'linear' or 'exponential'.")

  ema_name = f"{column}{suffix}"
  if not inplace:
      df = df.copy()

  df[ema_name] = df.ta.ema(close=column, length=length, smoothing=smoothing, offset=offset)

  return df

import pandas_ta as ta

def append_wma(df, column="Close", length=44, offset=0, suffix="_WMA", inplace=True):

    """
    Calculates and appends the Weighted Moving Average (WMA) to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the WMA will be calculated.
        column (str): Name of the column to use for calculating the WMA (default: "Close").
        length (int): Number of periods for the WMA calculation (default: 20).
        offset (int): Number of periods to shift the WMA forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new WMA column name (default: "_WMA").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: False).

    Returns:
        pandas.DataFrame: A DataFrame with the WMA appended as a new column.

    Raises:
        ValueError: If an invalid offset is provided.
    """

    if offset < 0:
        raise ValueError("Offset for WMA cannot be negative.")

    wma_name = f"{column}{suffix}"
    if not inplace:
        df = df.copy()

    df[wma_name] = df.ta.wma(close=column, length=length, offset=offset)

    return df


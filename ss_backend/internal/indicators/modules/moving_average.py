import pandas as pd
import pandas_ta as ta

def append_sma(df,**kwargs):
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

  column = kwargs.get("column", "close")
  length = kwargs.get("length", 50)
  offset = kwargs.get("offset", 0)

  if offset < 0:
      raise ValueError("Offset for SMA cannot be negative.")

  df.ta.sma(close=column, length=length, offset=offset,append=True)

  return df

def evaluate_sma(df, resultlist, **kwargs):
  """
  Evaluates the conditions and appends the DataFrame's symbol_id to a list of DataFrames if they meet the conditions.

  Args:
      df: The DataFrame to be evaluated.
      resultlist: A list of DataFrames where the symbol_id will be appended if the conditions are met.
      kwargs: A dictionary containing the following keys:
          - direction: "increasing" or "decreasing"
          - condition: "minimum", "maximum", or "exact"
          - bars: Number of bars to consider for the condition
          - additional_kwargs: Any additional keyword arguments passed to the function

  Returns:
      A list of DataFrames with the symbol_id appended if the conditions were met.
  """
  # Extract the conditions from kwargs
  conditions = {
      "direction": kwargs.get("direction"),
      "condition": kwargs.get("condition"),
      "bars": kwargs.get("bars"),
  }

#   print(df.tail(50))

# Check if the expected SMA column already exists
  sma_name = kwargs.get("name", "SMA") + "_" + str(kwargs.get("length"))
  if sma_name not in df.columns:
      raise ValueError(f"SMA column '{sma_name}' not found in the DataFrame.")

  # Use the existing SMA column for evaluation
  df['SMA'] = df[sma_name]

  # Check the direction
  if conditions['direction'] == "increasing":
      trend = df['SMA'] > df['SMA'].shift(1)
  else:
      trend = df['SMA'] < df['SMA'].shift(1)

  if conditions['condition'] == "minimum":
      minimum = df['SMA'].rolling(window=conditions['bars']).min()
      condition = df['SMA'] == minimum
  elif conditions['condition'] == "maximum":
      maximum = df['SMA'].rolling(window=conditions['bars']).max()
      condition = df['SMA'] == maximum
  else:
      # Check if SMA is increasing for exactly 5 bars
      condition = trend.iloc[-int(conditions['bars']):] # type: ignore

  # Check if the conditions are met
  if condition.iloc[-1]:
      resultlist.add(df["symbol_id"].iloc[0])

  return resultlist





def append_ema(df, **kwargs):
  """
  Calculates and appends the Exponential Moving Average (EMA) to a DataFrame.

  Args:
      df: The DataFrame where the EMA will be calculated.
      **kwargs: Dictionary containing any of the following optional parameters:
          - column: Name of the column to use for calculating the EMA (default: "close").
          - length: Number of periods for the EMA calculation (default: 20).
          - smoothing: Averaging method, either "linear" or "exponential" (default: "exponential").
          - offset: Number of periods to shift the EMA forward (positive) or backward (negative) (default: 0).
          - suffix: Suffix to add to the new EMA column name (default: "_EMA").
          - inplace: Whether to modify the original DataFrame or return a new one (default: False).

  Returns:
      A DataFrame with the EMA appended as a new column.

  Raises:
      ValueError: If an invalid smoothing method is provided.
  """

  column = kwargs.get("column", "close")
  length = kwargs.get("length", 50)
  smoothing = kwargs.get("smoothing", "exponential")
  offset = kwargs.get("offset", 0)


  if smoothing not in ("linear", "exponential"):
      raise ValueError("Invalid smoothing method. Choose 'linear' or 'exponential'.")


  df.ta.ema(close=column, length=length, smoothing=smoothing, offset=offset, append=True)

  return df

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

    df.ta.wma(close=column, length=length, offset=offset,append=True)

    return df


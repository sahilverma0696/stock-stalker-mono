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
  length = kwargs.get("length")
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

    df.ta.wma(close=column, length=length, offset=offset,append=True)

    return df

import pandas as pd

def calculate_mab(df, close="Close", window=20, std_dev=2):

    """
    Calculates Moving Average Bands (MAB) for a DataFrame and removes the MA and STD columns afterwards.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        close (str): Name of the column containing closing prices (default: "Close").
        window (int): Window size for the moving average (default: 20).
        std_dev (float): Number of standard deviations for the bands (default: 2).

    Returns:
        pandas.DataFrame: The original DataFrame with additional columns for the upper and lower bands.
    """

    # Calculate the moving average and standard deviation
    df["MA"] = df[close].rolling(window=window).mean()
    df["STD"] = df[close].rolling(window=window).std()

    # Calculate upper and lower bands
    df["UpperBand"] = df["MA"] + std_dev * df["STD"]
    df["LowerBand"] = df["MA"] - std_dev * df["STD"]

    # Remove MA and STD columns
    del df["MA"]
    del df["STD"]

    return df


def evaluate_ma(df, **kwargs):
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
  ma_name = str(kwargs.get("name")) + "_" + str(kwargs.get("length"))
  if ma_name not in df.columns:
      raise ValueError(f"MA column '{ma_name}' not found in the DataFrame.")


  # Check the direction
  if conditions['direction'] == "increasing":
      trend = df[ma_name] > df[ma_name].shift(1)
  else:
      trend = df[ma_name] < df[ma_name].shift(1)

  if conditions['condition'] == "minimum":
      minimum = df[ma_name].rolling(window=conditions['bars']).min()
      condition = df[ma_name] == minimum
  elif conditions['condition'] == "maximum":
      maximum = df[ma_name].rolling(window=conditions['bars']).max()
      condition = df[ma_name] == maximum
  else:
      # Check if MA is increasing for exactly 5 bars
      condition = trend.iloc[-int(conditions['bars']):] # type: ignore

  # Check if the conditions are met
  if condition.iloc[-1]:
      return True
  return False



def evaluate_ma_convergence(df, condition:dict,column:list):
  """
  Evaluates ma convergence condition.

  Args:
      df: The DataFrame to be evaluated.
      kwargs: A dictionary containing the following keys:
          - indicators: A list of dictionaries, each containing:
              - name: User-defined name for the SMA column.
          - condition: A dictionary containing:
              - difference: The difference threshold between SMA values.
              - type: "percentage" or "bars" for the difference calculation.
              - bars: Number of bars to consider for the difference calculation (optional, required for "bars" type only).

  Returns:
      True if the conditions are met, False otherwise.
  """

  # Get condition parameters
  condition_type = condition.get("type")
  threshold = int(condition.get("threshold")) # type: ignore
  bars = int(condition.get("bars")) # type: ignore


  # Calculate the difference based on the type
  if condition_type == "percentage":
      ## Where difference is less than percentage in last bars
      
      # Calculate pairwise differences
      df["differences"] = df[column].max(axis=1) - df[column].min(axis=1)

      # Calculate absolute values and convert to percentage
      df["differences"] = (df["differences"] / df[column].max(axis=1)) * 100
      
      # Check if the difference is less than 5 in the last 2 bars
      last_bars = df["differences"].iloc[-bars:]

      cond = last_bars < threshold
      if cond.any():
        return True
      else:
        return False
  elif condition_type == "bars":
       # Calculate pairwise differences
      differences = df[column].diff(axis=1)

      # Add the new column to the DataFrame
      df["abs_diff_in_bar"] = differences.abs().max(axis=1)

      # Get the last count_bars rows
      last_bars = df.iloc[-threshold:]

      # Check if the minimum value is within the last bars
      min_index = last_bars["abs_diff_in_bar"].idxmin()
      if (df.index[-1] - min_index).total_seconds() / 3600 <= bars:
          print(df.tail(10))
          return True
      else:
          return False

def evaluate_ma_crossover(df, sma_columns,condition:dict):
  """
  Evaluates if a specific crossover occurred in the last `lookback` bars.

  Args:
    df: A Pandas DataFrame containing the OHLCV data and the SMAs.
    sma_columns: A list of strings containing the names of the SMA columns.
    first_sma: The name of the first SMA column.
    crossover: The type of crossover to evaluate ("bullish" or "bearish").
    bars: The number of bars to look back for the crossover.

  Returns:
    True if the crossover occurred in the last `lookback` bars, False otherwise.
  """

  # Get condition parameters
  crossover = condition.get("crossover")
  first_sma = "SMA_"+str(condition.get("first")) # type: ignore
  bars = int(condition.get("bars")) # type: ignore


  # Calculate the crossover condition
  if crossover == "bullish":
    crossover_condition = df[first_sma] > df[sma_columns[1]]
  elif crossover == "bearish":
    crossover_condition = df[first_sma] < df[sma_columns[1]]
  else:
    raise ValueError("Invalid crossover type: {}".format(crossover))  

  # Check if the crossover occurred in the last `lookback` bars
  return crossover_condition.tail(bars).any()



def evaluate_ma_price_crossover(df, sma_column, condition:dict):
  """
  Evaluates if the price closed above or below the SMA in the last `lookback` bars.

  Args:
    df: A Pandas DataFrame containing the OHLCV data and the SMA.
    sma_column: The name of the SMA column.
    condition: The condition to evaluate ("above" or "below").
    bars: The number of bars to look back for the condition.

  Returns:
    True if the price closed above/below the SMA in any of the last `lookback` bars, False otherwise.
  """

  # Get condition parameters
  closed = condition.get("closed")
  bars = int(condition.get("bars")) # type: ignore


  # Calculate the price-SMA closed
  if closed == "above":
    price_sma_condition = df["close"] > df[sma_column[0]]
  elif closed == "below":
    price_sma_condition = df["close"] < df[sma_column[0]]
  else:
    raise ValueError("Invalid condition: {}".format(closed))
  
  # Check if the condition occurred in the last `lookback` bars
  return price_sma_condition.tail(bars).any()

def evaluate_mab(df, condition:dict):
  """
  Evaluates if the price or a full candle met the specified condition with respect to the UpperBand or LowerBand in the last `lookback` bars.

  Args:
    df: A Pandas DataFrame containing the OHLCV data and the Bollinger Bands.
    band_column: The name of the band column ("UpperBand" or "LowerBand").
    condition: The condition to evaluate ("price_above", "full_candle_above", "price_below", "full_candle_below", "supertrend_above", "supertrend_below").
    lookback: The number of bars to look back for the condition.

  Returns:
    True if the price or a full candle met the specified condition with respect to the band in any of the last `lookback` bars, False otherwise.
  """
  # Get condition parameters
  state = str(condition.get("state"))
  bars = int(condition.get("bars")) # type: ignore
  band_column = str(condition.get("band"))


  # Define the evaluation function based on the condition
  condition_functions = {
    "price_above": lambda df, band: df["close"] > df[band],
    "full_candle_above": lambda df, band: df["high"] > df[band],
    "price_below": lambda df, band: df["close"] < df[band],
    "full_candle_below": lambda df, band: df["low"] < df[band],
    ##TODO: SuperTrend is left
    "supertrend_above": lambda df, band: df["SuperTrend"] > df[band],
    "supertrend_below": lambda df, band: df["SuperTrend"] < df[band],
  }

  # Check if the condition occurred in the last `lookback` bars
  return condition_functions[state](df.tail(bars), band_column).any()
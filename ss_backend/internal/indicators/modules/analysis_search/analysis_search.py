import pandas as pd

def breakout_analysis(df, high="High", low="Low", close="Close", threshold=0.01):

  """
  Analyzes potential breakouts based on closing prices crossing above/below historical highs/lows.

  Args:
      df (pandas.DataFrame): The DataFrame containing price data.
      high (str): Name of the column containing high prices (default: "High").
      low (str): Name of the column containing low prices (default: "Low").
      close (str): Name of the column containing closing prices (default: "Close").
      threshold (float): Threshold for price difference considered significant (default: 0.01).

  Returns:
      pandas.DataFrame: The original DataFrame with additional columns indicating potential breakouts.
  """

  df["breakout_up"] = False
  df["breakout_down"] = False

  # Identify potential breakouts above historical highs

  previous_highs = df[high].rolling(window=20, min_periods=1).max()
  df["breakout_up"] = (df[close] > previous_highs) & (df[close] > df[close].shift(1))

  # Identify potential breakouts below historical lows

  previous_lows = df[low].rolling(window=20, min_periods=1).min()
  df["breakout_down"] = (df[close] < previous_lows) & (df[close] < df[close].shift(1))

  # Calculate percentage change for breakout events

  df["breakout_up_pct"] = (df[close] - previous_highs) / previous_highs * 100
  df["breakout_down_pct"] = (df[close] - previous_lows) / previous_lows * 100

  return df

import pandas as pd

def identify_pullback(df, close="Close", ma_column="MA", threshold=0.01):

    """
    Identifies potential pullbacks based on closing prices exceeding and retracing from a moving average.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        close (str): Name of the column containing closing prices (default: "Close").
        ma_column (str): Name of the column containing the moving average (default: "MA").
        threshold (float): Threshold for price difference considered significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with an additional column indicating potential pullbacks.
    """

    df["pullback"] = False

    # Identify exceeding points
    exceeding_points = df[close] > df[ma_column]

    # Identify pullback points
    pullback_points = exceeding_points & (df[close] < df[close].shift(1))

    # Mark identified pullbacks
    df.loc[pullback_points.index, "pullback"] = True

    return df

import pandas as pd

def pullback_trading_strategy(df, close="Close", ma_column="MA", entry_threshold=-0.02, exit_threshold=0.01):

    """
    Implements a simple pullback trading strategy based on moving average crossover and price retracement.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        close (str): Name of the column containing closing prices (default: "Close").
        ma_column (str): Name of the column containing the moving average (default: "MA").
        entry_threshold (float): Threshold for pullback price movement to trigger entry (default: -0.02).
        exit_threshold (float): Threshold for price movement to trigger exit (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with additional columns for entry and exit signals.
    """

    df["pullback"] = False
    df["entry_signal"] = False
    df["exit_signal"] = False

    # Identify pullback points
    pullback_points = df[close] > df[ma_column] & (df[close] < df[close].shift(1))

    # Identify entry points
    entry_points = pullback_points & ((df[close] / df[close].shift(1) - 1) < entry_threshold)

    # Identify exit points
    exit_points = (df[close] > df[close].shift(1)) & ((df[close] / df[close].shift(1) - 1) > exit_threshold)

    # Mark identified pullbacks, entry signals, and exit signals
    df.loc[pullback_points.index, "pullback"] = True
    df.loc[entry_points.index, "entry_signal"] = True
    df.loc[exit_points.index, "exit_signal"] = True

    return df

# import pandas as pd

# def identify_keyzones(df, high="High", low="Low", close="Close", support_column="Support", resistance_column="Resistance", threshold=0.01):

#     """
#     Identifies keyzones based on historical support and resistance levels.

#     Args:
#         df (pandas.DataFrame): The DataFrame containing price data.
#         high (str): Name of the column containing high prices (default: "High").
#         low (str): Name of the column containing low prices (default: "Low").
#         close (str): Name of the column containing closing prices (default: "Close").
#         support_column (str): Name of the column containing support levels (default: "Support").
#         resistance_column (str): Name of the column containing resistance levels (default: "Resistance").
#         threshold (float): Threshold for considering a price level significant (default: 0.01).

#     Returns:
#         pandas.DataFrame: The original DataFrame with keyzones marked by support and resistance columns.
#     """

#     # Identify support and resistance levels (using another function)
#     df = identify_support_resistance(df, high, low, close)

#     # Define keyzone range around support and resistance levels
#     df["keyzone_low"] = df[support_column] - threshold * (df[high] - df[low])
#     df["keyzone_high"] = df[resistance_column] + threshold * (df[high] - df[low])

#     return df

# import pandas as pd

# def identify_keyzone_bollinger(df, close="Close", bollinger_bands="BollingerBands", threshold=2):

#     """
#     Identifies keyzones based on the Bollinger Bands indicator.

#     Args:
#         df (pandas.DataFrame): The DataFrame containing price data.
#         close (str): Name of the column containing closing prices (default: "Close").
#         bollinger_bands (str): Name of the Bollinger Bands indicator (default: "BollingerBands").
#         threshold (float): Threshold for identifying keyzones based on standard deviations (default: 2).

#     Returns:
#         pandas.DataFrame: The original DataFrame with keyzones identified by Bollinger Bands.
#     """

#     # Identify Bollinger Bands (using another function)
#     df = add_bollinger_bands(df, close)

#     # Define keyzone based on upper and lower bands
#     df["keyzone_low"] = df[bollinger_bands]["lower_band"]
#     df["keyzone_high"] = df[bollinger_bands]["upper_band"]

#     # Optionally, adjust keyzone based on standard deviations
#     df["keyzone_low"] = df["keyzone_low"] - threshold * df[bollinger_bands]["std"]
#     df["keyzone_high"] = df["keyzone_high"] + threshold * df[bollinger_bands]["std"]

#     return df

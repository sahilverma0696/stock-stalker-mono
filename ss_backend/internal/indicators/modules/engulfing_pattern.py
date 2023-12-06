import pandas as pd

"""NOT PROOF"""

def identify_bullish_engulfing(df, column="Close", open="Open", low="Low", threshold=0.01):

    """
    Identifies potential Bullish Engulfing patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        column (str): Name of the column containing closing prices (default: "Close").
        open (str): Name of the column containing opening prices (default: "Open").
        low (str): Name of the column containing low prices (default: "Low").
        threshold (float): Threshold for considering a price difference significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with an additional column indicating potential Bullish Engulfing patterns.
    """

    df["bullish_engulfing"] = False

    # Identify bearish candle
    bearish_candle = df[df[column] < df[open]]

    # Identify next candle
    next_candle = bearish_candle.join(df.shift(-1))

    # Filter valid Bullish Engulfing patterns
    valid_patterns = next_candle.loc[
        (next_candle[column] > next_candle[open])
        & (next_candle[low] < bearish_candle[low] - threshold)
        & (next_candle[df.high] > bearish_candle[df.high] + threshold)
    ]

    df.loc[valid_patterns.index, "bullish_engulfing"] = True

    return df


def identify_bearish_engulfing(df, column="Close", open="Open", high="High", threshold=0.01):

    """
    Identifies potential Bearish Engulfing patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        column (str): Name of the column containing closing prices (default: "Close").
        open (str): Name of the column containing opening prices (default: "Open").
        high (str): Name of the column containing high prices (default: "High").
        threshold (float): Threshold for considering a price difference significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with an additional column indicating potential Bearish Engulfing patterns.
    """

    df["bearish_engulfing"] = False

    # Identify bullish candle
    bullish_candle = df[df[column] > df[open]]

    # Identify next candle
    next_candle = bullish_candle.join(df.shift(-1))

    # Filter valid Bearish Engulfing patterns
    valid_patterns = next_candle.loc[
        (next_candle[column] < next_candle[open])
        & (next_candle[high] < bullish_candle[high] - threshold)
        & (next_candle[df.low] > bullish_candle[df.low] + threshold)
    ]

    df.loc[valid_patterns.index, "bearish_engulfing"] = True

    return df

def identify_harami(df, column="Close", open="Open", threshold=0.01):

    """
    Identifies potential Harami patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        column (str): Name of the column containing closing prices (default: "Close").
        open (str): Name of the column containing opening prices (default: "Open").
        threshold (float): Threshold for considering a price difference significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with an additional column indicating potential Harami patterns.
    """

    df["harami"] = False

    # Identify engulfing candle
    engulfing_candle = df.loc[df[column].abs() > df[open].abs()]

    # Identify next candle
    next_candle = engulfing_candle.join(df.shift(-1))

    # Filter valid Harami patterns
    valid_patterns = next_candle.loc[
        (next_candle[column].abs() < engulfing_candle[open].abs() - threshold)
        & (next_candle[df.high] < engulfing_candle[df.high])
        & (next_candle[df.low] > engulfing_candle[df.low])
    ]

    df.loc[valid_patterns.index, "harami"] = True

    return df


import pandas as pd


def identify_piercing_line(df, column="Close", open="Open", low="Low", threshold=0.01):

    """
    Identifies potential Piercing Line patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        column (str): Name of the column containing closing prices (default: "Close").
        open (str): Name of the column containing opening prices (default: "Open").
        low (str): Name of the column containing low prices (default: "Low").
        threshold (float): Threshold for considering a price difference significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with an additional column indicating potential Piercing Line patterns.
    """

    df["piercing_line"] = False

    # Identify bearish candle
    bearish_candle = df[df[column] < df[open]]

    # Identify next candle
    next_candle = bearish_candle.join(df.shift(-1))

    # Filter valid Piercing Line patterns
    valid_patterns = next_candle.loc[
        (next_candle[open] < bearish_candle[low])
        & (next_candle[low] > bearish_candle[low])
        & (next_candle[df.high] > bearish_candle[df.high] + threshold)
        & (next_candle[column] > next_candle[open])
    ]

    df.loc[valid_patterns.index, "piercing_line"] = True

    return df

import pandas as pd


def identify_hammer_hanging_man(df, column="Close", open="Open", high="High", low="Low", threshold=0.01):

    """
    Identifies potential Hammer and Hanging Man patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        column (str): Name of the column containing closing prices (default: "Close").
        open (str): Name of the column containing opening prices (default: "Open").
        high (str): Name of the column containing high prices (default: "High").
        low (str): Name of the column containing low prices (default: "Low").
        threshold (float): Threshold for considering a price difference significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with additional columns indicating potential Hammer and Hanging Man patterns.
    """

    df["hammer"] = False
    df["hanging_man"] = False

    # Identify long lower shadow
    long_lower_shadow = df[df[low] < df[open] - threshold]

    # Identify small body
    small_body = df[abs(df[df.close] - df[open]) < threshold]

    # Identify potential Hammer and Hanging Man patterns
    hammer_candidates = long_lower_shadow.merge(small_body, on=df.index)
    hanging_man_candidates = long_lower_shadow.merge(small_body, on=df.index)

    # Filter valid Hammer patterns
    hammer_patterns = hammer_candidates.loc[
        (hammer_candidates[df.close] > hammer_candidates[open])
        & (hammer_candidates[high] - hammer_candidates[df.close]) < threshold * 2
    ]

    # Filter valid Hanging Man patterns
    hanging_man_patterns = hanging_man_candidates.loc[
        (hanging_man_candidates[df.close] < hanging_man_candidates[open])
        & (hanging_man_candidates[open] - hanging_man_candidates[low]) < threshold * 2
    ]

    # Mark identified patterns in the DataFrame
    df.loc[hammer_patterns.index, "hammer"] = True
    df.loc[hanging_man_patterns.index, "hanging_man"] = True

    return df


import pandas as pd


def identify_doji(df, column="Close", open="Open", threshold=0.01):

    """
    Identifies potential Doji patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        column (str): Name of the column containing closing prices (default: "Close").
        open (str): Name of the column containing opening prices (default: "Open").
        threshold (float): Threshold for considering price differences significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with an additional column indicating potential Doji patterns.
    """

    df["doji"] = False

    # Check for small price difference between open and close
    doji_candidates = df[abs(df[column] - df[open]) < threshold]

    # Filter valid Doji patterns
    valid_dojis = doji_candidates.loc[
        (doji_candidates[df.high] - doji_candidates[df.low])
        > threshold * 2
    ]

    df.loc[valid_dojis.index, "doji"] = True

    return df

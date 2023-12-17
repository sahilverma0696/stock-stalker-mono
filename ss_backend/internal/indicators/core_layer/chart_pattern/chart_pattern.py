import pandas as pd


def identify_double_top(df, column="Close", high="High", threshold=0.01):

    """
    Identifies potential double top patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        column (str): Name of the column containing closing prices (default: "Close").
        high (str): Name of the column containing high prices (default: "High").
        threshold (float): Threshold for considering a price difference significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with an additional column indicating potential double top patterns.
    """

    df["double_top"] = False

    # Identify first peak
    first_peak = df.loc[df[high] == df[high].max()]

    # Identify potential second peak
    second_peak_candidates = df.loc[df.index > first_peak.index]

    # Filter valid second peak
    second_peak = second_peak_candidates.loc[
        (
            (second_peak_candidates[high] == df[high].max())
            & (second_peak_candidates[high] - first_peak[high]) < threshold
        )
        & (second_peak_candidates.index > first_peak.index + 1)
    ]

    # Filter valid double top patterns
    valid_double_tops = first_peak.append(second_peak)

    # Mark identified patterns in the DataFrame
    df.loc[valid_double_tops.index, "double_top"] = True

    return df

import pandas as pd


def identify_triple_top(df, column="Close", high="High", threshold=0.01):

    """
    Identifies potential triple top patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        column (str): Name of the column containing closing prices (default: "Close").
        high (str): Name of the column containing high prices (default: "High").
        threshold (float): Threshold for considering a price difference significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with an additional column indicating potential triple top patterns.
    """

    df["triple_top"] = False

    # Identify first peak
    first_peak = df.loc[df[high] == df[high].max()]

    # Identify potential second peak
    second_peak_candidates = df.loc[df.index > first_peak.index]

    # Filter valid second peak
    second_peak = second_peak_candidates.loc[
        (
            (second_peak_candidates[high] == df[high].max())
            & (second_peak_candidates[high] - first_peak[high]) < threshold
        )
        & (second_peak_candidates.index > first_peak.index + 1)
    ]

    # Identify potential third peak
    third_peak_candidates = df.loc[df.index > second_peak.index]

    # Filter valid third peak
    third_peak = third_peak_candidates.loc[
        (
            (third_peak_candidates[high] == df[high].max())
            & (third_peak_candidates[high] - first_peak[high]) < threshold
        )
        & (third_peak_candidates.index > second_peak.index + 1)
    ]

    # Filter valid triple top patterns
    valid_triple_tops = first_peak.append(second_peak).append(third_peak)

    # Mark identified patterns in the DataFrame
    df.loc[valid_triple_tops.index, "triple_top"] = True

    return df

import pandas as pd


def identify_double_bottom(df, column="Close", low="Low", threshold=0.01):

    """
    Identifies potential double bottom patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        column (str): Name of the column containing closing prices (default: "Close").
        low (str): Name of the column containing low prices (default: "Low").
        threshold (float): Threshold for considering a price difference significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with an additional column indicating potential double bottom patterns.
    """

    df["double_bottom"] = False

    # Identify first trough
    first_trough = df.loc[df[low] == df[low].min()]

    # Identify potential second trough
    second_trough_candidates = df.loc[df.index > first_trough.index]

    # Filter valid second trough
    second_trough = second_trough_candidates.loc[
        (
            (second_trough_candidates[low] == df[low].min())
            & (second_trough_candidates[low] - first_trough[low]) < threshold
        )
        & (second_trough_candidates.index > first_trough.index + 1)
    ]

    # Filter valid double bottom patterns
    valid_double_bottoms = first_trough.append(second_trough)

    # Mark identified patterns in the DataFrame
    df.loc[valid_double_bottoms.index, "double_bottom"] = True

    return df


import pandas as pd


def identify_triple_bottom(df, column="Close", low="Low", threshold=0.01):

    """
    Identifies potential triple bottom patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        column (str): Name of the column containing closing prices (default: "Close").
        low (str): Name of the column containing low prices (default: "Low").
        threshold (float): Threshold for considering a price difference significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with an additional column indicating potential triple bottom patterns.
    """

    df["triple_bottom"] = False

    # Identify first trough
    first_trough = df.loc[df[low] == df[low].min()]

    # Identify potential second trough
    second_trough_candidates = df.loc[df.index > first_trough.index]

    # Filter valid second trough
    second_trough = second_trough_candidates.loc[
        (
            (second_trough_candidates[low] == df[low].min())
            & (second_trough_candidates[low] - first_trough[low]) < threshold
        )
        & (second_trough_candidates.index > first_trough.index + 1)
    ]

    # Identify potential third trough
    third_trough_candidates = df.loc[df.index > second_trough.index]

    # Filter valid third trough
    third_trough = third_trough_candidates.loc[
        (
            (third_trough_candidates[low] == df[low].min())
            & (third_trough_candidates[low] - first_trough[low]) < threshold
        )
        & (third_trough_candidates.index > second_trough.index + 1)
    ]

    # Filter valid triple bottom patterns
    valid_triple_bottoms = first_trough.append(second_trough).append(third_trough)

    # Mark identified patterns in the DataFrame
    df.loc[valid_triple_bottoms.index, "triple_bottom"] = True

    return df


import pandas as pd


def identify_support_resistance(df, high="High", low="Low", close="Close", window=20):

    """
    Identifies potential support and resistance levels based on swing points.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        high (str): Name of the column containing high prices (default: "High").
        low (str): Name of the column containing low prices (default: "Low").
        close (str): Name of the column containing closing prices (default: "Close").
        window (int): The window size for swing detection (default: 20).

    Returns:
        pandas.DataFrame: The original DataFrame with additional columns for support and resistance levels.
    """

    df["swing_highs"] = df[high].rolling(window=window, min_periods=1).max()
    df["swing_lows"] = df[low].rolling(window=window, min_periods=1).min()

    support_levels = []
    resistance_levels = []

    for i in range(len(df)):
        # Check for support level
        if (
            df["swing_lows"][i] == df["low"][i]
            and df["close"][i] > df["close"][i - 1]
        ):
            support_levels.append(df["low"][i])

        # Check for resistance level
        if (
            df["swing_highs"][i] == df["high"][i]
            and df["close"][i] < df["close"][i - 1]
        ):
            resistance_levels.append(df["high"][i])

    df["support"] = support_levels
    df["resistance"] = resistance_levels

    return df

import pandas as pd


# def identify_wolfe_wave(df, high="High", low="Low", close="Close", threshold=0.01):

#     """
#     Identifies potential Wolfe Wave patterns in a DataFrame.

#     Args:
#         df (pandas.DataFrame): The DataFrame containing price data.
#         high (str): Name of the column containing high prices (default: "High").
#         low (str): Name of the column containing low prices (default: "Low").
#         close (str): Name of the column containing closing prices (default: "Close").
#         threshold (float): Threshold for considering a price difference significant (default: 0.01).

#     Returns:
#         pandas.DataFrame: The original DataFrame with additional columns indicating potential Wolfe Wave patterns.
#     """

#     df["wolfe_wave"] = False

#     # Identify potential wave 1
#     wave1_candidates = df.loc[(df[high] - df[low]) > df[close] * threshold]

#     # Filter valid wave 1
#     wave1 = wave1_candidates.loc[(wave1_candidates[close] > wave1_candidates[open])]

#     # Identify potential wave 2
#     wave2_candidates = df.loc[df.index > wave1.index]

#     # Filter valid wave 2
#     wave2 = wave2_candidates.loc[(wave2_candidates[low] < wave1[low]) & (wave2[close] < wave1[close])]

#     # Identify potential wave 3
#     wave3_candidates = df.loc[df.index > wave2.index]

#     # Filter valid wave 3
#     wave3 = wave3_candidates.loc[
#         (wave3[high] > wave2[high]) & (wave3[low] < wave1[low]) & (wave3[close] > wave2[close])
#     ]

#     # Identify potential wave 4
#     wave4_candidates = df.loc[df.index > wave3.index]

#     # Filter valid wave 4
#     wave4 = wave4_candidates.loc[
#         (
#             (wave4[low] < wave3[low])
#             & (wave4[close] < wave3[close])
#             & (wave4[low] > (wave1[low] + wave2[low]) / 2)
#         )
#     ]

#     # Identify potential wave 5
#     wave5_candidates = df.loc[df.index > wave4.index]

#     # Filter valid wave 5
#     wave5 = wave5_candidates.loc[
#         (wave5[high] > wave4[high]) & (wave5[close] > wave4[close]) & (wave5[high] > wave1[high])
#     ]

#     # Filter valid Wolfe Wave patterns
#     valid_wolfe_waves = wave1.append(wave2).append(wave3).append(wave4).append(wave5)

#     # Mark identified patterns in the DataFrame
#     df.loc[valid_wolfe_waves.index, "wolfe_wave"] = True

#     return df

import pandas as pd


def identify_abcd(df, high="High", low="Low", close="Close", threshold=0.01):

    """
    Identifies potential AB=CD harmonic patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        high (str): Name of the column containing high prices (default: "High").
        low (str): Name of the column containing low prices (default: "Low").
        close (str): Name of the column containing closing prices (default: "Close").
        threshold (float): Threshold for considering a price difference significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with an additional column indicating potential AB=CD patterns.
    """

    df["abcd"] = False

    # Identify point A (highest high)
    point_a = df[high] == df[high].max()

    # Identify point B (trough after A)
    point_b = df.loc[point_a.index + 1, low] == df[low].min()

    # Identify point C (peak after B)
    point_c = df.loc[point_b.index + 1, high] == df[high].max()

    # Calculate AB and CD lengths
    ab_length = df[high][point_a] - df[low][point_b]
    cd_length = df[high][point_c] - df[low][point_c + 1]

    # Check AB=CD condition
    is_abcd = (
        point_a
        & point_b
        & point_c
        & ((cd_length <= ab_length) | (cd_length <= (1 + threshold) * ab_length))
    )

    # Mark identified patterns in the DataFrame
    df.loc[is_abcd.index, "abcd"] = True

    return df


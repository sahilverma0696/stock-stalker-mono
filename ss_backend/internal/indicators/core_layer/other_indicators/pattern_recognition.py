"""NOT PROOF"""

import pandas as pd

def identify_head_and_shoulders(df, column="Close", high="High", low="Low", threshold=0.01):

    """
    Identifies potential Head and Shoulders (H&S) patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        column (str): Name of the column containing closing prices (default: "Close").
        high (str): Name of the column containing high prices (default: "High").
        low (str): Name of the column containing low prices (default: "Low").
        threshold (float): Threshold for considering a price difference significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with additional columns indicating potential H&S patterns.
    """

    # Define additional columns to store H&S information
    df["head_peak"] = False
    df["left_shoulder"] = False
    df["right_shoulder"] = False

    # Identify left shoulder
    left_shoulder = df[df[high] == df[high].max() - 1]
    left_shoulder = left_shoulder.loc[(left_shoulder[column] - df[column]) > threshold]
    df.loc[left_shoulder.index, "left_shoulder"] = True

    # Identify head
    head_peak = df[df[high] == df[high].max()]
    df.loc[head_peak.index, "head_peak"] = True

    # Identify right shoulder
    right_shoulder = df[df[high] == df[high].max() + 1]
    right_shoulder = right_shoulder.loc[(df[column] - right_shoulder[column]) > threshold]
    df.loc[right_shoulder.index, "right_shoulder"] = True

    # Identify potential H&S patterns based on identified peaks
    df["head_and_shoulders"] = (
        df["left_shoulder"] & df["head_peak"] & df["right_shoulder"]
    )

    return df


def identify_triangles(df, column="Close", high="High", low="Low", threshold=0.01):

    """
    Identifies potential triangle patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        column (str): Name of the column containing closing prices (default: "Close").
        high (str): Name of the column containing high prices (default: "High").
        low (str): Name of the column containing low prices (default: "Low").
        threshold (float): Threshold for considering a price difference significant (default: 0.01).

    Returns:
        pandas.DataFrame: The original DataFrame with additional columns indicating potential triangle patterns.
    """

    # Define additional columns to store triangle information
    df["rising_triangle"] = False
    df["falling_triangle"] = False
    df["symmetrical_triangle"] = False

    # Identify rising triangle
    rising_triangle = df[
        (df[column].diff() > threshold)
        & (df[high].diff() < threshold)
        & (df[low].diff() > threshold)
    ]
    df.loc[rising_triangle.index, "rising_triangle"] = True

    # Identify falling triangle
    falling_triangle = df[
        (df[column].diff() < -threshold)
        & (df[high].diff() > -threshold)
        & (df[low].diff() < -threshold)
    ]
    df.loc[falling_triangle.index, "falling_triangle"] = True

    # Identify symmetrical triangle
    symmetrical_triangle = df[
        (df[high].diff() < threshold)
        & (df[high].diff() > -threshold)
        & (df[low].diff() < threshold)
        & (df[low].diff() > -threshold)
    ]
    df.loc[symmetrical_triangle.index, "symmetrical_triangle"] = True

    return df

import pandas as pd


def identify_cup_and_handle(df, column="Close", high="High", low="Low", threshold=0.01, min_cup_depth=0.05, max_cup_duration=14, min_handle_duration=3, max_handle_duration=7):

    """
    Identifies potential Cup and Handle (C&H) patterns in a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing price data.
        column (str): Name of the column containing closing prices (default: "Close").
        high (str): Name of the column containing high prices (default: "High").
        low (str): Name of the column containing low prices (default: "Low").
        threshold (float): Threshold for considering a price difference significant (default: 0.01).
        min_cup_depth (float): Minimum depth of the cup as a percentage of the overall price range (default: 0.05).
        max_cup_duration (int): Maximum duration of the cup formation in periods (default: 14).
        min_handle_duration (int): Minimum duration of the handle formation in periods (default: 3).
        max_handle_duration (int): Maximum duration of the handle formation in periods (default: 7).

    Returns:
        pandas.DataFrame: The original DataFrame with an additional column indicating potential C&H patterns.
    """

    df["cup_and_handle"] = False

    # Identify cup formation
    cup_lows = df[df[low] == df[low].min()]
    cup_depth = (df[high].max() - cup_lows[low]) / df[high].max()

    # Filter valid cup formations
    valid_cup_lows = cup_lows.loc[(cup_depth >= min_cup_depth) & (cup_lows.index.diff() <= max_cup_duration)]

    # Identify handle
    for i in valid_cup_lows.index:
        handle_high = df[i:].loc[(df[high] - df[i][high]) < threshold, high].max()
        handle_low = df[i:].loc[(df[low] - df[i][low]) < threshold, low].min()
        if handle_high is not None and handle_low is not None:
            handle_duration = df[i:].index[df[high] == handle_high][0] - i
            if min_handle_duration <= handle_duration <= max_handle_duration:
                df.loc[i:i + handle_duration, "cup_and_handle"] = True

    return df

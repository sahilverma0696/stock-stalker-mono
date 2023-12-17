
import pandas_ta as ta


def append_stochastic_oscillator(df, column="Close", k_length=14, d_length=3, offset=0, suffix="_SO", inplace=True):
    """
    Calculates and appends the Stochastic Oscillator (SO) to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the Stochastic Oscillator will be calculated.
        column (str): Name of the column to use for calculating the Stochastic Oscillator (default: "Close").
        k_length (int): Number of periods for the %K calculation (default: 14).
        d_length (int): Number of periods for the %D smoothing (default: 3).
        offset (int): Number of periods to shift the Stochastic Oscillator forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new Stochastic Oscillator column names (default: "_SO").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the Stochastic Oscillator appended as new columns (in-place modification).
    """

    if not inplace:
        raise ValueError(
            "The `append_stochastic_oscillator` function only supports in-place modification (inplace=True).")

    # Calculate the %K and %D values of the Stochastic Oscillator
    so_k = df.ta.stoch(close=column, high=column, low=column,
                       k_length=k_length, d_length=d_length, offset=offset, append=True)


def append_momentum_oscillator(df, column="Close", length=14, k_length=10, d_length=3, offset=0, suffix="_MO", inplace=True):
    """
    Calculates and appends the Momentum Oscillator to a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame where the Momentum Oscillator will be calculated.
        column (str): Name of the column to use for calculating the Momentum Oscillator (default: "Close").
        length (int): Number of periods for the momentum calculation (default: 14).
        k_length (int): Number of periods for the %K calculation (default: 10).
        d_length (int): Number of periods for the %D smoothing (default: 3).
        offset (int): Number of periods to shift the Momentum Oscillator forward (positive) or backward (negative) (default: 0).
        suffix (str): Suffix to add to the new Momentum Oscillator column names (default: "_MO").
        inplace (bool): Whether to modify the original DataFrame or return a new one (default: True).

    Returns:
        pandas.DataFrame: The DataFrame with the Momentum Oscillator appended as new columns (in-place modification).
    """

    if not inplace:
        raise ValueError(
            "The `append_momentum_oscillator` function only supports in-place modification (inplace=True).")

    # Calculate the momentum
    momentum = df.ta.momentum(close=column, length=length, append=True)

    # Calculate the %K and %D values of the Momentum Oscillator
    df.ta.stoch(close=column, high=column, low=column,
                k_length=k_length, d_length=d_length, offset=offset, append=True)

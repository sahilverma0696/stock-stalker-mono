"""
Contains function mapper, which returns the function and params on given by functionName,
functionName is expected to be provided in API call, along with that specific parameter
"""

from internal.indicators.modules.bollinger_band import append_bollinger_bands
from internal.indicators.modules.moving_average import append_ema, append_sma, append_wma

IndicatorMap ={
    "sma": append_sma,
    "ema": append_ema,
    "wma": append_wma,
    "bband":append_bollinger_bands,
}

# def propertiesFactory():

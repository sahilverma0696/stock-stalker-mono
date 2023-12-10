'''
This is the orchestrator layer, will get all the functions and make them happen in sequence here

'''

from internal.indicators.modules.moving_average import append_sma
from internal.indicators.modules.dataframes import getDataFrameMap

def smaOrch(symbols:list,condition:dict)->list:
          
    result =[] # contains list of resultant symbols
    
    # df = getDataFrameMap(["SBIN","YESBANK","CHENNPETRO"],100)
    # simpleMovingAverage(df,column_lower,window)

    # df["SMA_44_rising"] = df["SMA_44"].gt(df["SMA_44"].shift(1))

    return []

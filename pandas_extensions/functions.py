import pandas as pd 


def could_merge(df1, df2):
    """Naive check for whether DataFrames can merge"""
    memory = {}
    for column in df1.columns:
        memory[column] = True 
    for column in df2.columns:
        if column in memory:
            return column 
    return None
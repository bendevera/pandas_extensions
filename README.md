# pandas_extensions

author: Ben de Vera

view at: https://test.pypi.org/project/pandas-extensions/0.1/

## classes

### SuperDataFrame

Extension of the pandas.DataFrame class that adds additional methods.

    - SuperDataFrame.null_report

        - Displays number of null values in each column of a pandas.DataFrame

        - Params
            self : pandas.DataFrame
            verbose : boolean

    - SuperDataFrame.train_test_val_split

        - Provides a train/test/val split of a pandas.DataFrame

        - Params 
            self : pandas.DataFrame
            train_size : float 
            test_size : float
            verbose : boolean

## functions 

### could_merge

Naive check for whether DataFrames can merge

Params
    df1 : pandas.DataFrame
    df2 : pandas.DataFrame
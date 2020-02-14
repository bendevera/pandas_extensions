import pandas as pd 

class SuperDataFrame(pd.DataFrame):
    """
    Extension of the pandas.DataFrame class that adds additional methods.
    """

    def null_report(self, verbose=False):
        """
        Displays number of null values in each column of a pandas.DataFrame

        Params
            self : pandas.DataFrame
            verbose : boolean
        """
        if verbose:
            print("-"*8 + " NULL REPORT " + "-"*8)
        memory = {}
        for column in iter(self.columns):
            curr_count = self[column].isnull().sum()
            memory[column] = curr_count
            if verbose:
                print(f"{column} null count: {curr_count}")
        return memory

    def train_test_val_split(self, train_size=.7, test_size=.15, verbose=False):
        """
        Provides a train/test/val split of a pandas.DataFrame

        Params 
            self : pandas.DataFrame
            train_size : float 
            test_size : float
            verbose : boolean
        """
        if train_size + test_size >= 1:
            raise ValueError
        train_end = int(train_size * self.shape[0])
        test_end = train_end + int(test_size * self.shape[0])
        data = self.copy()
        train = data[:train_end]
        test = data[train_end:test_end]
        val = data[test_end:]
        if verbose:
            print("TRAIN/TEST/VAL Breakdown:")
            print(f"TRAIN : {train.shape}")
            print(f"TEST : {test.shape}")
            print(f"VAL : {val.shape}")
        return train, test, val


if __name__ == "__main__":
    TEST_CSV = "/Users/bendevera/Desktop/development/data_science/SuperDataFrame/books.csv"
    df = pd.read_csv(TEST_CSV)
    df = SuperDataFrame(df)
    df.null_report()
    train, test, val = df.train_test_val_split()
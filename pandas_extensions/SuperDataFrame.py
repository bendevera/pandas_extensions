import pandas as pd 

class SuperDataFrame(pd.DataFrame):
    """
    Extension of the pandas.DataFrame class that adds additional methods.
    """

    def df_null_report(self):
        """
        Displays number of null values in each column of a pandas.DataFrame

        Params
            self : pandas.DataFrame
        """
        print("-"*8 + " NULL REPORT " + "-"*8)
        for column in self.columns:
            print(f"{column} null count: ", self[column].isnull().sum())

    def train_test_val_split(self):
        """
        Provides a train/test/val split of a pandas.DataFrame

        Params 
            self : pandas.DataFrame
        """
        train_end = int(.7 * self.shape[0])
        print(0, train_end)
        test_end = train_end + int(.15 * self.shape[0])
        print(train_end, test_end)
        print(train_end+test_end, self.shape[0])
        train = self[:train_end]
        test = self[train_end:test_end]
        val = self[test_end:]
        print("TRAIN/TEST/VAL Breakdown:")
        print(f"TRAIN : {train.shape}")
        print(f"TEST : {test.shape}")
        print(f"VAL : {val.shape}")
        return train, test, val


if __name__ == "__main__":
    TEST_CSV = "/Users/bendevera/Desktop/development/data_science/SuperDataFrame/books.csv"
    df = pd.read_csv(TEST_CSV)
    df = SuperDataFrame(df)
    df.df_null_report()
    train, test, val = df.train_test_val_split()
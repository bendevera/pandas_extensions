import unittest
from pandas_extensions import SuperDataFrame
import pandas as pd


TEST_CSV = "/Users/bendevera/Desktop/development/data_science/SuperDataFrame/books.csv"

class DataFrameTest(unittest.TestCase):
    """
    Tests the SuperDataFrame class
    """

    def test_null_report(self):
        df = SuperDataFrame(pd.read_csv(TEST_CSV))
        null_report = df.null_report()
        self.assertTrue(null_report['original_title'] == 585)
    
    def test_split(self):
        df = SuperDataFrame(pd.read_csv(TEST_CSV))
        train, test, val = df.train_test_val_split() 

        self.assertEqual(train.shape, (7000, 23))
        self.assertEqual(test.shape, val.shape, (1500, 23))



if __name__ == "__main__":
    unittest.main()
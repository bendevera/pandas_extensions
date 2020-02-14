import unittest
from pandas_extensions import SuperDataFrame
from pandas_extensions import could_merge
import pandas as pd


TEST_CSV = "/Users/bendevera/Desktop/development/data_science/SuperDataFrame/books.csv"

class PandasExtensionsTest(unittest.TestCase):
    """
    Tests the pandas_extensions package.
    """

    df = SuperDataFrame(pd.read_csv(TEST_CSV))

    def test_null_report(self):
        null_report = self.df.null_report()
        self.assertTrue(null_report['original_title'] == 585)
    
    def test_split(self):
        train, test, val = self.df.train_test_val_split() 

        self.assertEqual(train.shape, (7000, 23))
        self.assertEqual(test.shape, val.shape, (1500, 23))
    
    def test_could_merge(self):
        self.df = SuperDataFrame(pd.read_csv(TEST_CSV))
        df2 = SuperDataFrame(pd.read_csv(TEST_CSV))
        result = could_merge(self.df, df2)
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
import os
import unittest
from company import *

class MyTest(unittest.TestCase):
    def test(self):
        file = os.path.join(os.path.dirname(__file__), 'test.csv')
        stock_highest = getHighestPrices(file)
        output = {
                  'Company3': {'price': 20.0, 'month': 'Jan', 'year': '1990'},
                   'Company2': {'price': 95.0, 'month': 'June', 'year': '1990'},
                    'Company1': {'price': 75.0, 'month': 'Apr', 'year': '1990'}
                }
        assert stock_highest == output

if __name__ == '__main__':
    unittest.main()


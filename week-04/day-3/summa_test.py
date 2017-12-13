import unittest
from summa import Summ


class SummaTest(unittest.TestCase):
    def test_sum_of_numbers(self):
        my_list = Summ()
        self.assertEqual(my_list.sum_of_numbers([1, 4, 5]), 10)
    
    def test_sum_of_empty(self):
        my_list = Summ()
        self.assertEqual(my_list.sum_of_numbers([]), 0)
        
    def test_sum_of_one_item(self):
        my_list = Summ()
        self.assertEqual(my_list.sum_of_numbers([1]), 1)
        
    def test_sum_of_none(self):
        my_list = Summ()
        self.assertEqual(my_list.sum_of_numbers([0]), 0)

if __name__ == '__main__':
    unittest.main()
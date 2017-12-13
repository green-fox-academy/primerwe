import unittest
from apples import *

class AppleTest(unittest.TestCase):
    def test_apple_equals(self):
        self.assertEqual(pear.get_apple(), 'apple')
    

if __name__ == '__main__':
    unittest.main()
import unittest
from fibonacci import fibonacci

class FibonacciTest(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(12), 144)

    def test_fibonacci_for_zero(self):
        self.assertEqual(fibonacci(0), 0)

if __name__ == '__main__':
    unittest.main()
import unittest
from count_letter import count_letters

class LetterCountTest(unittest.TestCase):
    def test_for_empty_string(self):
        self.assertEqual(count_letters(""), {})
        
    def test_for_one_item(self):
        self.assertEqual(count_letters("a"), {"a" : 1})

    def test_for_multiple_item(self):
        self.assertEqual(count_letters("greenfox"), {"g" : 1, "r" : 1, "e" : 2, "n" : 1, "f" : 1, "o" : 1, "x" : 1})

if __name__ == '__main__':
    unittest.main()
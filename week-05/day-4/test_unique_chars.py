import unittest
from unique_chars import unique_characters

class UniqueCharactersTest(unittest.TestCase):
    
    def test_for_empty_string(self):
        self.assertEqual(unique_characters(""), [])
        
    def test_for_upper_chars(self):
        self.assertEqual(unique_characters("ANAGRAMMS"), ["n", "g", "r", "s"])

    def test_for_multiple_item(self):
        self.assertEqual(unique_characters("green fox"), ["g", "r", "n", "f", "o", "x"])
    
if __name__ == '__main__':
    unittest.main()
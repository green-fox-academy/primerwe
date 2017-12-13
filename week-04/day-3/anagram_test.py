import unittest
from anagram import is_anagram

class AnagramTest(unittest.TestCase):
    def test_for_one_word(self):
        self.assertEqual(is_anagram('greenfox', 'regexfon'), True)
        
    def test_for_multiple_word(self):
        self.assertEqual(is_anagram('green fox', 'regex fon'), True)
        
    def test_for_whitespaces(self):
        self.assertEqual(is_anagram('green fox', 'reg ex fon'), True)
        
    def test_for_upper_lower_case(self):
        self.assertEqual(is_anagram('Green Fox', 'Reg Ex Fon'), True)
    
    def test_for_not_anagram(self):
        self.assertEqual(is_anagram('ann', 'annn'), False)
    
if __name__ == '__main__':
    unittest.main()
import unittest
from sharpie import Sharpie

class SharpieTest(unittest.TestCase):
    def test_sharpie(self):
        sharpie1 = Sharpie('black', 0.7)
        self.assertEqual(sharpie1.ink_amount,100)
        self.assertEqual(sharpie1.color,'black')
        self.assertEqual(sharpie1.width, 0.7)
        
    def test_sharpie_use(self):
        sharpie1 = Sharpie('black', 0.7)
        sharpie1.use()
        self.assertEqual(sharpie1.ink_amount, 90)
    
if __name__ == '__main__':
    unittest.main()
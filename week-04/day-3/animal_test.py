import unittest
from animal import Animal

class AnimalTest(unittest.TestCase):
    def test_animal(self):
        animal1 = Animal()
        self.assertEqual(animal1.hunger, 50)
        self.assertEqual(animal1.thirst, 50)
        
    def test_animal_eat(self):
        animal1 = Animal()
        animal1.eat()
        self.assertEqual(animal1.hunger, 49)
    
    def test_animal_drink(self):
        animal1 = Animal()
        animal1.drink()
        self.assertEqual(animal1.thirst, 49)
    
    def test_animal_play(self):
        animal1 = Animal()
        animal1.play()
        self.assertEqual(animal1.thirst, 51)
        self.assertEqual(animal1.hunger, 51)
    
if __name__ == '__main__':
    unittest.main()
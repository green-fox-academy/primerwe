class Animal(object):
    def __init__(self, hunger = 50, thirst = 50):
        self.hunger = hunger
        self.thirst = thirst
        
    def eat(self):
        self.hunger -= 1
        return self.hunger
    
    def drink(self):
        self.thirst -= 1
        return self.thirst
    
    def play(self):
        self.hunger += 1
        self.thirst += 1
        return self.hunger
        return self.thirst
    
animal1 = Animal()
animal2 = Animal()
animal3 = Animal()

animal1.play()
print(animal1.hunger)
print(animal1.thirst)
animal2.drink()
print(animal2.thirst)
animal1.eat()
animal1.eat()
animal1.eat()
print(animal1.hunger)
animal3.eat()
print(animal3.hunger)
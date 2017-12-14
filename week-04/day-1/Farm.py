from Animal import Animal

class Farm():
    def __init__(self, slot):
        self.animal = []
        self.slot = slot
        
    def add(self, animal):
        if self.slot > 0:
            self.animal.append(animal)
            self.slots -= 1
            
    def breed(self, hunger=50, thirst=50):
        if self.slots > 0:
            new_animal = Animal(hunger, thirst)
            self.animal.append(new_animal)
            self.slots -= 1
            
    def slaughter(self):
        self.animal.sort(key=lambda x: x.hunger, reverse=False)
        del self.animal[0]
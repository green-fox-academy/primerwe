class Garden(object):
    def __init__(self, plants = []):
        self.plants = plants
        
    def add_plant(self, plant):
        if plant not in self.plants:
            self.plants.append(plant)
    
    def watering(self, water):
        counter = 0
        for i in self.plants:
            if i.plant_type == 'Flower' and i.water_amount < 5 or i.plant_type == 'Tree' and i.water_amount < 10:
                counter += 1
        water = water / counter
        for i in self.plants:
            if i.plant_type == 'Flower' and i.water_amount < 5:
                i.water_amount += water * 0.75
            if i.plant_type == 'Tree' and i.water_amount < 10:
                i.water_amount += water * 0.4
        print("Watering with " + str(int(water * counter)))

class Flower():
    def __init__(self, color, plant_type = 'Flower', water_amount = 0):
        self.color = color
        self.plant_type = plant_type
        self.water_amount = water_amount
    
    def status(self):
        if self.water_amount < 5:
            print("The " + format(self.color) + " " + format(self.plant_type) + " needs water")
        else:
            print("The " + format(self.color) + " " + format(self.plant_type) + " doesnt needs water")


class Tree():
    def __init__(self, color, plant_type = 'Tree', water_amount = 0):
        self.color = color
        self.plant_type = plant_type
        self.water_amount = water_amount
    
    def status(self):
        if self.water_amount < 10:
            print("The " + format(self.color) + " " + format(self.plant_type) + " needs water")
        else:
            print("The " + format(self.color) + " " + format(self.plant_type) + " doesnt needs water")
            

yellow = Flower('yellow')
blue = Flower('blue')
purple = Tree('purple')
orange = Tree('orange')

yellow.status()
blue.status()
purple.status()
orange.status()

garden = Garden()
garden.add_plant(yellow)
garden.add_plant(blue)
garden.add_plant(purple)
garden.add_plant(orange)

garden.watering(40)
yellow.status()
blue.status()
purple.status()
orange.status()

garden.watering(70)
yellow.status()
blue.status()
purple.status()
orange.status()
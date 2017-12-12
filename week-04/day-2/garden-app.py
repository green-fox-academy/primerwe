class Garden(object):
    def __init__(self, flowers = [], trees = []):
        self.flowers = flowers
        self.trees = trees
        
    def add_flower(self, flower):
        if flower not in self.flowers:
            self.flowers.append(flower)
    
    def add_tree(self, tree):
        if tree not in self.trees:
            self.trees.append(tree)

    
        

class Flower(Garden):
    def __init__(self, color, plant_type = 'Flower', water_amount = 0):
        self.color = color
        self.plant_type = plant_type
        self.water_amount = water_amount
    
    def status(self):
        if self.water_amount < 5:
            print("The " + format(self.color) + " " + format(self.plant_type) + " needs water")
        else:
            print("The " + format(self.color) + " " + format(self.plant_type) + " doesnt needs water")


class Tree(Garden):
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
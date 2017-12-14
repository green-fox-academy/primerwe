class Sharpie(object):
    def __init__(self, color, width, ink_amount=100):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount
    
    def use(self):
        self.ink_amount -= 10
        return self.ink_amount
    
    def print_status(self):
        print("Color: " + format(self.color) + ", width: " + format(self.width) + ", ink amount: " + format(self.ink_amount))


red = Sharpie("red", 1.25)
green = Sharpie("#b4dc47", 0.7)
blue = Sharpie("#00f", 1.0)
black = Sharpie("#000", 2.5, 0)

list_of_sharpies = [red, green, blue, black]

for i in range(len(list_of_sharpies)):
    list_of_sharpies[i].print_status()

red.use()

for i in range(len(list_of_sharpies)):
    list_of_sharpies[i].print_status()
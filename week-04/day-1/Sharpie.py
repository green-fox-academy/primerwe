class Sharpie(object):
    def __init__(self, color, width, ink_amount=100):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount
    
    def use(self):
        self.ink_amount -= 10
        return self.ink_amount

red = Sharpie("red", 1.25)
green = Sharpie("#b4dc47", 0.7)
blue = Sharpie("#0000ff", 1.0)

print("Color: " + red.color + ", width: " + str(red.width) + ", ink amount: " + str(red.ink_amount))

red.use()

print("Color: " + red.color + ", width: " + str(red.width) + ", ink amount: " + str(red.ink_amount))
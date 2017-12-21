# We run a Candy shop where we sell candies and lollipops
# One lollipop's price is 10$
# And it made from 5gr of sugar
# One candie's price is 20$
# And it made from 10gr of sugar
# we can raise their prices with a given percentage
#
# Create a CandyShop class
# It can store sugar and money as income. The constructor should take the amount of sugar in gramms.
# we can create lollipops and candies store them in the CandyShop's storage
# If we create a candie or lollipop the CandyShop's sugar amount gets reduced by the amount needed to create the sweets
# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candie or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"
class CandyShop(object):
    def __init__(self, sugar_amount):
        self.sugar_amount = sugar_amount
        self.income = 0
        self.candy_count = 0
        self.lollipop_count = 0
    
    def create_sweets(self, type_of):
        if type_of == "candy":
            self.sugar_amount -= 10
            self.candy_count += 1
        if type_of == "lollipop":
            self.sugar_amount -= 5
            self.lollipop_count += 1
        
    def sell(self, type_of, amount):
        if type_of == "candy":
            self.candy_count -= amount
            self.income += candy.price
        if type_of == "lollipop":
            self.lollipop_count -= amount
            self.income += lollipop.price
    
    def raise_prices(self, percentage):
        candy.price += candy.price * percentage / 100
        lollipop.price += lollipop.price * percentage / 100
    
    def buy_sugar(self, amount):
        self.sugar_amount += amount
        self.income -= amount / 10
        
    def __str__(self):
        return "Invetory: {} candies, {} lollipops, Income: {}, Sugar: {}gr".format(self.candy_count, self.lollipop_count, self.income, self.sugar_amount)
        
        
class Sweets():
    def __init__(self, type_of="", price=0, sugar_content=0):
        self.type_of = type_of
        self.price = price
        self.sugar_content = sugar_content
        if type_of == "candy":
            self.price = 20
            self.sugar_content = 10
        if type_of == "lollipop":
            self.price = 10
            self.sugar_content = 5

candy = Sweets("candy", 20, 10)
lollipop = Sweets("lollipop", 10, 5)
             
candy_shop = CandyShop(300)
candy_shop.create_sweets("candy")
candy_shop.create_sweets("candy")
candy_shop.create_sweets("lollipop")
candy_shop.create_sweets("lollipop")
print(candy_shop)
# Should print out:
# Invetory: 2 candies, 2 lollipops, Income: 0, Sugar: 270gr
candy_shop.sell("candy", 1)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 2 lollipops, Income:20, Sugar: 270gr"
candy_shop.raise_prices(5)
candy_shop.sell("lollipop", 1)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:30.5, Sugar: 270gr"
candy_shop.buy_sugar(300)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:0.5, Sugar: 570gr"
class Car(object):
    def __init__(self, gas_amount = 0, capacity = 100):
        self.gas_amount = gas_amount
        self.capacity = capacity

    
class Station(object):
    def __init__(self, gas_amount):
        self.gas_amount = gas_amount
    
    def refill_car(self, car):
        self.gas_amount -= car.capacity
        car.gas_amount += car.capacity
    
car1 = Car()
station1 = Station(1000)
print(station1.gas_amount)
station1.refill_car(car1)
print(station1.gas_amount)
print(car1.gas_amount)
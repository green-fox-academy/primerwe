class Aircraft():
    def __init__(self, aircraft_type, ammo_store = 0, max_ammo, base_damage)
        self.aircraft_type = aircraft_type
        self.ammo_store = ammo_store
        self.max_ammo = max_ammo
        self.base_damage = base_damage
        if aircraft_type == 'F16':
            max_ammo = 8
            base_damage = 30
        if aircraft_type == 'F35':
            max_ammo = 12
            base_damage = 50
        
    def fight(self):
        self.ammo_store -= max_ammo
        damage = (self.max_ammo * self.base_damage)
        return damage
    
    def refill(self, ammo):
        if self.ammo > self.max_ammo:
            self.ammo -= max_ammo
            return self.ammo
    
    def get_type(self):
        print(format.(self.aircraft_type))
    
    def get_status(self):
        print("Type: " + format(self.aircraft_type) + ", " + "Ammo: " + format(self.ammo_store) + ", " + "Base Damage: " + format(self.base_damage) + ", " + "All Damage: " + str(damage))

class AircraftCarrier(object):
    def __init__(self, aircrafts = [], ammo_storage, ammo = 1000, health_point = 5000):
        self.aircrafts = aircrafts
        self.ammo_storage = ammo_storage
        self.ammo = ammo
        self.health_point = health_point
        
    def add_aircraft(self, aircraft):
        if aircraft not in self.aircrafts:
            self.aircrafts.append(aircraft)
    
    def fill(self):
        
    def fight(self, carrier):
        
    def get_status(self):
        total_damage = 0
        for i in self.aircrafts:
            total_damage += (i.max_ammo * i.base_damage)
            i += 1
        if self.health_point == 0:
            print("It's dead Jim :(")
        else:
            print("HP: " + format(self.health_point) + ", Aircraft count: " + str(len(self.aircrafts)) + ", Ammo Storage: " + format(self.ammo_storage) + ", Total damage: " + str(total_damage) + "\n Aircrafts:\n")
            for i in self.aircrafts:
                print(i.arcrafts.get_status(aircraft))
        
        
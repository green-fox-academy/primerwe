class Aircraft():
    def __init__(self, aircraft_type, ammo = 0, max_ammo = 0, base_damage = 0)
        self.aircraft_type = aircraft_type
        self.ammo = ammo
        self.max_ammo = max_ammo
        self.base_damage = base_damage
        if aircraft_type == 'F16':
            self.max_ammo = 8
            self.base_damage = 30
        if aircraft_type == 'F35':
            self.max_ammo = 12
            self.base_damage = 50
        
    def fight(self):
        damage = (self.max_ammo * self.base_damage)
        self.ammo = 0
        return damage
    
    def refill(self, number):
        if number > self.max_ammo:
            self.ammo = self.max_ammo
            return number - self.max_ammo
    
    def get_type(self):
        return self.aircraft_type
    
    def get_status(self):
        print("Type: " + format(self.aircraft_type) + ", " + "Ammo: " + format(self.ammo) + ", " + "Base Damage: " + format(self.base_damage) + ", " + "All Damage: " + format(self.damage * self.ammo))


class AircraftCarrier(object):
    def __init__(self, aircrafts = [], initial_ammo = 100, health_point = 5000):
        self.aircrafts = aircrafts
        self.initial_ammo = initial_ammo
        self.health_point = health_point
        
    def add_aircraft(self, aircraft):
        if aircraft not in self.aircrafts:
            self.aircrafts.append(aircraft)
    
    def fill(self):
        if self.initial_ammo == 0:
            print("No ammunition left!")
            return
        f16 = 0
        f35 = 0
        for i in range(len(self.aircrafts)):
            if self.aircrafts[i].aircraft_type == "F16":
                f16 += 1
            elif self.aircrafts[i].aircraft_type == "F35":
                f35 += 1
        needed_ammo = f16*8 + f35*12
        if needed_ammo > self.initial_ammo:
            for i in range(len(self.aircrafts)):
                if self.aircrafts[i].aircraft_type == "F35" and self.initial_ammo >= self.aircrafts[i].max_ammo:
                    self.aircrafts[i].ammo = self.aircrafts[i].max_ammo
                    self.initial_ammo = self.initial_ammo - self.aircrafts[i].max_ammo
                elif self.aircrafts[i].type == "F35" and 0 < self.initial_ammo < self.aircrafts[i].max_ammo:
                    self.aircrafts[i].ammo = self.initial_ammo
                    self.initial_ammo = 0
            if self.initial_ammo > 0:
                for i in range(len(self.aircrafts)):
                    if self.aircrafts[i].aircraft_type == "F16" and self.initial_ammo >= self.aircrafts[i].max_ammo:
                        self.aircrafts[i].ammo = self.aircrafts[i].max_ammo
                        self.initial_ammo = self.initial_ammo - self.aircrafts[i].max_ammo
                    elif self.aircrafts[i].aircraft_type == "F16" and 0 < self.initial_ammo < self.aircrafts[i].max_ammo:
                        self.aircrafts[i].ammo = self.initial_ammo
                        self.initial_ammo = 0
        else:
            for i in range(len(self.aircrafts)):
                self.aircrafts[i].ammo = self.aircrafts[i].max_ammo
                self.initial_ammo = self.initial_ammo - self.aircrafts[i].max_ammo
        
    def fight(self, carrier):
        damage = 0
        for i in range(len(self.aircrafts)):
            damage += self.aircrafts[i].base_damage * self.aircrafts[i].ammo
        carrier.health_point -= damage
        if carrier.health_point <= 0 and self.health_point > 0:
            print("Victory")
        elif carrier.health_point > 0 and self.health_point > 0:
            print("Continues")
        elif self.health_point <= 0:
            print("Defeat")
        
    def get_status(self):
        total_damage = 0
        for i in range(len(self.aircrafts)):
            total_damage += (self.aircrafts[i].max_ammo * self.aircrafts[i].base_damage)
        if self.health_point == 0:
            print("It's dead Jim :(")
            return
        else:
            print("HP: " + format(self.health_point) + ", Aircraft count: " + str(len(self.aircrafts)) + ", Ammo Storage: " + format(self.initial_ammo) + ", Total damage: " + str(total_damage))
        print("Aircrafts:")
        for i in range(len(self.aircrafts)):
            print("Type " + format(self.aircrafts[i].aircraft_type) + ", Ammo: " + format(self.aircrafts[i].ammo) + ", Base Damage: " + format(self.aircrafts[i].base_damage) + ", All damage: " + format(self.aircrafts[i].base_damage * self.aircrafts[i].ammo))
        
        
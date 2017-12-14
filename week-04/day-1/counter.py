class Counter(object):
    def __init__(self, field_value = 0):
        self.field_value = field_value
        
    def add(self, number = 1):
        self.field_value += number
    
    def get(self):
        return self.field_value
    
    def reset(self):
        self.field_value = 0
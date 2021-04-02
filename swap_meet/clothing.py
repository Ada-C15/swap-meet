from swap_meet.item import Item

class Clothing(Item):
    
    def __init__(self, condition=None, age=None):
        self.category = "Clothing"
        self.condition = condition
        self.age = age

    def __str__(self):
        return "The finest clothing you could wear."
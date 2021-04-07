from .item import Item

class Clothing(Item):
    def __init__(self, age = None, category = "Clothing", condition = 0):
        super().__init__(age, category, condition)

        
    def __str__(self):
        return "The finest clothing you could wear."   

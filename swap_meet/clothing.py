from .item import Item

class Clothing(Item):
    def __init__(self, category = None):
        if category == None:
            self.category = "Clothing"
        else:
            self.category = "Clothing"
    

    
    def __str__(self):
        return "The finest clothing you could wear."
from .item import Item
class Clothing(Item):
    def __init__(self, category = "", condition = None):
        
        super().__init__(category = "", condition = None)
        self.category = "Clothing"
        self.condition = condition
    
    def __str__(self):
        return "The finest clothing you could wear."
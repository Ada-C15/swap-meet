from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition = None, age = None): # took category out and passed it in through super. Back to my original working way.
        super().__init__("Clothing", condition, age)
        #self.category = "Clothing"
    
    def __str__(self):
        return "The finest clothing you could wear."
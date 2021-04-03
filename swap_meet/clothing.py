from swap_meet.item import Item

class Clothing(Item): 
    def __init__(self, category="", condition=0): 
        # self.category = "Clothing"
        # self.condition = float(condition)
        super().__init__("Clothing", condition)
    # def __init__(self, category="", condition=0): 

    def __str__(self): 
        return "The finest clothing you could wear."

# ----------- WAVE 4 -----------
from swap_meet.item import Item
class Clothing(Item):
    def __init__ (self):
        super()
        self.category = "Clothing"
        # self.condition = 0
    
    def __str__(self):
        return "The finest clothing you could wear."
    # def condition_description(self,condition):
    #     if item 



# ----------- WAVE 4 -----------
from swap_meet.item import Item
class Clothing(Item):
    def __init__ (self, condition=0, category ="Clothing"):
        super().__init__("Clothing", condition)
        self.category = "Clothing"
        self.condition = condition
    
    def __str__(self):
        return "The finest clothing you could wear."

    # def condition_description(self):
    #     return super().condition_description()



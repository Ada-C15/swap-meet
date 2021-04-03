from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition=None):
        self.category = "Clothing"
        if condition == None:
            self.condition = 0
        else:
            self.condition = float(condition)
    
    def condition_description(self):
        super().condition_description(self)

    def __str__(self):
        return "The finest clothing you could wear."
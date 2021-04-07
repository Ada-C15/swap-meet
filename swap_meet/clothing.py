from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition = 0):
        self.category = "Clothing"
        self.condition = float(condition)

    def __str__(self):
        if str(Clothing):
            return "The finest clothing you could wear."



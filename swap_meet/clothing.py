from swap_meet.item import Item

class Clothing(Item):

    def __init__(self, condition = None ):
        self.category = "Clothing"
        if condition:
            self.condition = float(condition)
        else:
            self.condition = 0

    def __str__(self):
        return "The finest clothing you could wear."

from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, category = None, condition = 0, year = 0):
        super().__init__("Clothing", condition, year)

    def __str__(self):
        return "The finest clothing you could wear."
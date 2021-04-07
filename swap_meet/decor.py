from swap_meet.item import Item
class Decor(Item):
    def __init__(self, category = None, condition = 0, year = 0):
        super().__init__("Decor", condition, year)

    def __str__(self):
        return "Something to decorate your space."
from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition = 0):
        self.category = "Decor"
        self.condition = float(condition)

    def __str__(self):
        if str(Decor):
            return "Something to decorate your space."



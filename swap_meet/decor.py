from swap_meet.item import Item

class Decor(Item):


    def __init__(self, condition = None):
        self.category = "Decor"
        if condition:
            self.condition = float(condition)
        else:
            self.condition = ""

    def __str__(self):
        return "Something to decorate your space."

# WAVE 5

from .item import Item

class Decor(Item):

    def __init__(self, category = "", condition = 0): 
        self.category = "Decor"
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."































    # def __init__(self):
    #     Item.__init__(self, "Decor")
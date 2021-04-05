from .item import Item
class Decor(Item):
    def __init__(self, category = "Decor", condition = None):

        super().__init__(category = "", condition = None)
        self.category = "Decor"
        self.condition = condition
    
    def __str__(self):
        return "Something to decorate your space."
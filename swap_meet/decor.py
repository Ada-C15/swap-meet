from .item import Item



class Decor(Item):
    def __init__(self, category = None):
        if category == None:
            self.category = "Decor"
        else:
            self.category = "Decor"
    
    def __str__(self):
        return "Something to decorate your space."
    
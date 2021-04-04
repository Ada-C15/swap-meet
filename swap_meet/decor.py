from .item import Item

class Decor(Item):
    def __init__(self, condition = 0):
        super().__init__(condition = condition)
        self.category = "Decor"
##Q1: why do I need to declare condition = 0 if its inheriting that from parent?  
##Q2: why do I need to set condition = to condition for it to accept float?      

    def __str__(self):
        return "Something to decorate your space."  
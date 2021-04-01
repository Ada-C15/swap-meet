from .item import Item

class Decor(Item):
    
    def __init__(self, category="", condition=None):
        super().__init__(self, condition)
        self.category = "Decor"
    
    def __str__(self):
        return "Something to decorate your space."

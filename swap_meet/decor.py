from .item import Item



class Decor(Item):
    def __init__(self, condition = None, age = None):
            category = "Decor"
            super().__init__(category, condition, age)
        
        
    
    def __str__(self):
        return "Something to decorate your space."
    
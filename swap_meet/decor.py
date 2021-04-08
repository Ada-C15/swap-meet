from .item import Item
class Decor(Item):
    def __init__(self, condition =0):
        '''constructs an instance of Decor,
        which is an instance of Item,
        with a default condition of 0'''

        super().__init__("Decor", condition)
       
    
    def __str__(self):
        '''prints message for class'''

        return "Something to decorate your space."
    
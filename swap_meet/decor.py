
from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category = "", condition = 0):
        self.category = "Decor"
        self.condition = condition

    def __str__(self):
        ''' 
        reassigns the stringified item
        '''
        return "Something to decorate your space."


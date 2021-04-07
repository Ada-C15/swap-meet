from swap_meet.item import Item

# ---- Wave 5 ----- #
class Decor(Item):
    '''
    Represents a decor Item
    Attributes: 
        category (str)
        condition (int/float)
        age (int/float)
    '''
    def __init__(self, condition=0, age=0): 
        '''
        Inherits methods of the parent class Item
        Parameters: 
            category ("Decor")
            condition (int/float)
            age (int/float)
        '''
        super().__init__("Decor",condition, age)

    def __str__(self): 
        '''
        Stringifies an instance of Decor 
        '''
        return "Something to decorate your space."


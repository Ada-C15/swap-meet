from swap_meet.item import Item

# ---- Wave 5 ----- #
class Electronics(Item):
    '''
    Represents a electronic Item
    Attributes: 
        category (str)
        condition (int/float)
        age (int/float)
    '''
    def __init__(self, category="", condition=0, age=0): 
        '''
        Inherits methods of the parent class Item
        Parameters: 
            category ("Electronics")
            condition (int/float)
            age (int/float)
        '''
        super().__init__("Electronics",condition, age)

    def __str__(self): 
        '''
        Stringifies an instance of Electronics
        '''
        return "A gadget full of buttons and secrets."
    
from swap_meet.item import Item

# ---- Wave 5 ----- #
class Clothing(Item):
    '''
    Represents a clothing Item
    Attributes: 
        category (str)
        condition (int/float)
        age (int/float)
    '''
    def __init__(self, category="", condition=0, age=0): 
        '''
        Inherits methods of the parent class Item
        Parameters: 
            category ("Clothing")
            condition (int/float)
            age (int/float)
        '''
        super().__init__("Clothing", condition, age)

    def __str__(self): 
        '''
        Stringifies an instance of Clothing 
        '''
        return "The finest clothing you could wear."


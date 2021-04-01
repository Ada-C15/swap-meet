from .item import Item


class Clothing(Item):
    def __init__(self, condition = None):
        self.category = "Clothing"
        if condition == None:
            self.condition = 0
        else:
            self.condition = condition
    
    '''
    This function is created to customize the string representation 
    of this self instance.
    Python call __str__ method automatically when str() is called,
    then overrides its str() method to return "The finest clothing 
    you could wear."
    '''
    def __str__(self):
        return "The finest clothing you could wear."



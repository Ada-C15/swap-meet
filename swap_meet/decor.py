from .item import Item


class Decor(Item):
    def __init__(self, condition = None, edge = None):
        super().__init__("Decor", condition, edge)
    
    '''
    This function is created to customize the string representation 
    of this self instance.
    Python call __str__ method automatically when str() is called,
    then overrides its str() method to return "Something to decorate 
    your space."
    '''
    def __str__(self):
        return "Something to decorate your space."
    


class Item:
    def __init__(self, category = None):
        if category == None:
            self.category = ""
        else:
            self.category = category
    
    '''
    This function is created to customize the string representation 
    of this self instance.
    Python call __str__ method automatically when str() is called,
    then overrides its str() method to return "Hello World!"
    '''
    def __str__(self):
        return "Hello World!"
    
    





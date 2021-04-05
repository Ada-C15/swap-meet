
class Item:
    # There is an Item class in an item module, which has a 'category' attribute that is initialized as an empty string
    def __init__(self, category=""):
        self.category = category
    
    # `Item` overrides its stringify method
    def __str__(self):
        return "Hello World!"
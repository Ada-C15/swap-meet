class Item:
    def __init__(self, category = ""):
        self.category = category
    
    def __str__(self):
        return "Hello World!"


# When we stringify an instance of Item using str(), it returns "Hello World!"
# This implies Item overrides its stringify method
  



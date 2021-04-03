# from .vendor import Vendor
# ---- Wave 2 ----- #
class Item:
    def __init__(self, category=None): 
        if category == None: 
            self.category = ""
        else: 
            self.category = category 

# ---- Wave 3 ----- #
    def __str__(self): 
        return "Hello World!"

    

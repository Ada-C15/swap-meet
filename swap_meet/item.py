from swap_meet.vendor import Vendor

class Item:
    def __init__(self, category=""):
        self.category = category

    # abstract method
    def __str__(self): 
        return "Hello World!"

        

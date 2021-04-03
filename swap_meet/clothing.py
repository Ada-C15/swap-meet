from swap_meet.item import Item
from swap_meet.vendor import Vendor


class Clothing:
    def __init__(self,condition=None):
        if condition==None:
        
            self.category="Clothing"
        else:
            self.condition=condition
    
    def __str__(self):
        return "The finest clothing you could wear."
    

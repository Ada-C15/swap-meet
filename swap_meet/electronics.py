from swap_meet.item import Item
from swap_meet.vendor import Vendor


class Electronics(Item):
    """ Child class inherits condition descriptions from Items class"""
    
    def __init__(self,category="",condition=None):
        self.category="Electronics"
        self.condition=condition

            
    def __str__(self):
        return "A gadget full of buttons and secrets."
    
 

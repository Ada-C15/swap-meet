from swap_meet.item import Item
from swap_meet.vendor import Vendor


class Clothing(Item):
    """ Child class inherits condition descriptions from Items class"""
    def __init__(self,category="",condition=None):
        self.category="Clothing"
        self.condition=condition
        
    
    def __str__(self):
       
        return "The finest clothing you could wear."
       

   

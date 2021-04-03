from swap_meet.item import Item
from swap_meet.vendor import Vendor


class Decor:
    def __init__(self,condition=None):
        if condition==None:
        
            self.category="Decor"
        else:
            self.condition=condition
    
    def __str__(self):
        return "Something to decorate your space."
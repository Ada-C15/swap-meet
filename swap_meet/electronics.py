from swap_meet.item import Item
from swap_meet.vendor import Vendor


class Electronics:
    def __init__(self,condition=None):
        if condition==None:
        
            self.category="Electronics"
        else:
            self.condition=condition
    
    def __str__(self):
        return "A gadget full of buttons and secrets."
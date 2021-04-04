from swap_meet.item import Item
from swap_meet.vendor import Vendor


class Electronics(Item):
    
    def __init__(self,condition=None):
        self.category="Electronics"
        if condition==None:
        
            self.condition=0
        else:
            self.condition=float(condition)
            
    def __str__(self):
        return "A gadget full of buttons and secrets."
    

    def condition_description(self):
        
        return super().condition_description() 

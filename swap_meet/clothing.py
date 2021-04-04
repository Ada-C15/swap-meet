from swap_meet.item import Item
from swap_meet.vendor import Vendor


class Clothing(Item):

    def __init__(self,condition=None):
        self.category="Clothing"
        if condition == None:
        
            self.condition=0
    
        else:
            self.condition=float(condition)
        
    
    def __str__(self):
       
        return "The finest clothing you could wear."
       
    def condition_description(self):
        
        return super().condition_description() 
   

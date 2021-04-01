#___________________WAVE 2_____________________________
#from swap_meet.vendor import Vendor

class Item:
    def __init__(self, category = None, condition = None):
        
        if category is None:
           self.category = ""
        else:
            self.category = category
        
        if condition is None:
            self.condition = 0
        else:
            self.condition = condition
            
#___________________WAVE 3_________________________________           
            
    def __str__(self):
         return "Hello World!"
     
#__________________WAVE 5_______________________________
    def condition_description(self):
    
        if self.condition >= 0 and  self.condition <= 2.5:
            return "Heavily used"
        elif self.condition > 2.5 and self.condition <= 3.5:
            return "moderate use"
        elif self.condition > 3.5 and self.condition <= 5.0:
            return "mint condition"
    
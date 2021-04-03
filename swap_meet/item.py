#___________________WAVE 2_____________________________
#from swap_meet.vendor import Vendor

class Item:
    def __init__(self, category = None, condition = None, age = None):
        
        if category is None:
           self.category = ""
        else:
            self.category = category
        
        if condition is None:
            self.condition = 0
        else:
            self.condition = condition
        #_______________optional enhancement______________
               
        if age is None:
            self.age = 0
        else:
            self.age = age
            
#___________________WAVE 3_________________________________           
            
    def __str__(self):
         return "Hello World!"
     
#__________________WAVE 5___________________________________
    def condition_description(self):
    
        if self.condition >= 0 and  self.condition <= 2.5:
            return "Heavily used"
        elif self.condition > 2.5 and self.condition <= 3.5:
            return "moderate use"
        elif self.condition > 3.5 and self.condition <= 5.0:
            return "mint condition"

#________________optional Enhancement_________________________
    def age_description(self):
        
        if  self.age >= 0 and  self.age <= 2:
            return "very new"
        elif self.condition > 1 and self.condition <= 4:
            return "like new"
        elif self.condition > 4 and self.condition <= 6:
            return "old"
        elif self.condition > 6:
            return "antique"
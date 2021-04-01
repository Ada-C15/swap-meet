#___________________wave 2_____________________________
#from swap_meet.vendor import Vendor

class Item:
    def __init__(self, category = ""):
        self.category = category
        self.condition = 0
        
    def __str__(self):
         return "Hello World!"
    
    def condition_description(self):
        for self.condition in range(0, 6):
            if self.condition in range(0, 2):
                print("Heavily used")
            elif self.condition in range (2, 4):
                print("moderate use")
            elif self.condition in range (4, 6):
                print("mint condition")
        
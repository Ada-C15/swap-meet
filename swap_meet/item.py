#from swap_meet.vendor import Vendor


class Item:
    def __init__(self, category = None):
        
        if category == None:
            self.category = ""
            
        else:
            self.category = category
    


    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5.0:
            return "That is so FETCH!"
        else:
            return "YOU CAN'T SIT WITH US!"
   




           



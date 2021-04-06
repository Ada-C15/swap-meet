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
            return "That is so FETCH! 💅🏽"
        elif self.condition== 4.0:
            return "Great choice, I see you're not like a regular mom, you're a cool mom! 👩‍👧‍👦"
        elif self.condition== 3.0:
            return "Get in loser, we're going swapping 🙀"
        elif self.condition == 2.0:
            return "Oh dear...may the force be with you 🙊"
        else:
            return "Really?? YOU CAN'T SIT WITH US! 🙅‍♀️"
   




           



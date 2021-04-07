# this will be the parent class
class Item:
    def __init__(self, condition = 0, category = ""):
        self.category = category
        self.condition = condition
    def __str__(self):
        return "Hello World!"    
    
    
    def condition_description(self):
        if self.condition >= 5:
            return "BRAND NEW - STRAIGHT OUT OF THE BOX"
        elif self.condition >= 4:
            return "Looks Brand New" 
        elif self.condition >= 3:
            return "A few imperfections - Nobody's Perfect!"
        elif self.condition >= 1:
            return "Fairly Used, Easy DIY fix"  






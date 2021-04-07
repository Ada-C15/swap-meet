#wave2
class Item():   #parens allow inheritance
    def __init__(self, category, condition=0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return("Hello World!")
    
    def condition_description(self):
        if self.condition == 0:
            return("bad")
        if self.condition == 1:
            return("very bad")
        if self.condition == 2:
            return("medium good")
        if self.condition == 3:
            return("good")
        if self.condition == 4:
            return("very good")
        if self.condition == 5:
            return("excellent")
    

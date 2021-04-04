class Item:
    def __init__(self, age = 0, condition = 0, category = None):
        if category == None:
            self.category = ""
        else:
            self.category = category
        self.condition = condition
        self.age = age

    def __str__ (self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "Trash"
        elif self.condition == 1:
            return "Y tho"
        elif self.condition == 2:
            return "Not the worst I've seen"
        elif self.condition == 3:
            return "Dece piece"
        elif self.condition == 4:
            return "oOoOoOo~!"
        elif self.condition == 5:
            return "Oh you fancy huh"
    
        
        
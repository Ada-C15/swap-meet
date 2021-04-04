# Swap Meet
# Ada Cohort 15 - Paper
# Katrina Kimzey (she|they)
# Started March 31, 2021

class Item:
    def __init__(self, category = "", condition = 0, age = 0):
        self.category = category 
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition >= 5:
            return "Minty fresh! New packaging and no fingerprints"
        elif self.condition == 4:
            return "New in box, but someone looked at it funny on the way here"
        elif self.condition == 3:
            return "Slightly used and very functional. Maybe clean before using."
        elif self.condition == 2:
            return "Holding together just enough to ask for money."
        elif self.condition == 1:
            return "My mother says it's got character."
        elif self.condition == 0:
            return "Probably best if it goes in the bin..."
        else:
            return "Unknown condition: Possibly haunted."

class Item:
    # wave 02 & 05
    def __init__(self, category="", condition=0.0):
        self.category = category
        self.condition = condition

    # wave 03
    def __str__(self):
        return "Hello World!"
    
    # wave 05
    def condition_description(self):
        if self.condition == 0:
            return "I am brand new!"
        elif self.condition == 1:
            return "I am fairly new."
        elif self.condition == 2:
            return "I am second hand but in a good condition."
        elif self.condition == 3:
            return "I am heavily used."
        elif self.condition == 4:
            return "I am in a bad condition!"
        else:
            return "I am broken..."


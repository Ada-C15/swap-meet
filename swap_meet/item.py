
# WAVE 2

class Item:
    
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition


# WAVE 3

    def __str__(self):
        return "Hello World!"


# WAVE 5

    def condition_description(self):
        if self.condition < 0 or self.condition > 5:
            return False
        elif self.condition == 0:
            return "Has seen much, much better days"
        elif self.condition == 1:
            return "Could work if you're desperate"
        elif self.condition == 2:
            return "Needs some TLC"
        elif self.condition == 3:
            return "Don't overthink it"
        elif self.condition == 4:
            return "Probably the best you can get"
        else:
            return "You've hit the motherload!"
        



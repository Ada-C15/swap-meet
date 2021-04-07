
class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition 

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition <= 0:
            return "Bad Condition"
        elif self.condition < 3:
            return "Okay Condition"
        elif self.condition < 4:
            return "Lightly Used"
        else:
            return "New"
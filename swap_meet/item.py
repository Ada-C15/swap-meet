class Item:
    pass
    def __init__(self, category="", condition = 0.0):
        self.category = category
        self.condition = condition
    def __str__(self):
        return "Hello World!"
    def condition_description(self): 
        if self.condition == 0:
            return "mint condition"
        elif self.condition == 1:
            return "like new"
        elif self.condition == 2:
            return "gently used"
        elif self.condition == 3:
            return "used"
        elif self.condition == 4:
            return "clean this before using it"
        elif self.condition == 5:
            return "Please clean 2x over"


    
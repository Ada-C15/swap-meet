class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = float(condition)

    def __str__(self):
        return 'Hello World!'
    def __repr__(self):
        return "Item('{}')".format(self.category)
    
    def condition_description(self):
        if self.condition == 5:
            desc = "mint"
        elif self.condition == 4:
            desc = "excellent"
        elif self.condition == 3:
            desc = "good"
        elif self.condition == 2:
            desc = "well used"
        elif self.condition == 1:
            desc = "Might use a glove"
        elif self.condition == 0:
            desc = "Make sure you really want to do this!"
        return desc
        
            
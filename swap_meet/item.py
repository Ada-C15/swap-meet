class Item:
    
    def __init__(self, category="", condition=None):
        if category == "":
            self.category = ""
        else:
            self.category = category
        
        if condition == None:
            self.condition = 0
        else:
            self.condition = condition 

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "You'd be a sucker to buy this"
        elif 0 < self.condition <= 1:
            return "Poor"
        elif 1 < self.condition <= 2:
            return "Very used"
        elif 2 < self.condition <= 3:
            return "Used"
        elif 3 < self.condition <= 4:
            return "Gently used"
        else:
            return "Top knotch"

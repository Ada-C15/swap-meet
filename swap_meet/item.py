class Item:
    def __init__(self, category=None):
        if category == None:
            self.category = ""
        else:
            self.category = category
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 1.0:
            return "Not in the best shape, but still usable!"
        elif self.condition == 2.0:
            return "Has received a lot of love, and could definitely use more!"
        elif self.condition == 3.0:
            return "In fair condition! Definitely not the worst thing on the shelf!"
        elif self.condition == 4.0:
            return "Very lightly used, but not mint condition."
        elif self.condition == 5.0:
            return "Like new! It's your lucky day!!"
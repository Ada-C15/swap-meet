# WAVE TWO

class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition 

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition > 4.0 :
            return "Mint condition"
        elif self.condition > 3.0 :
            return "Gently used"
        elif self.condition > 2.0:
            return "Kinda broken but it'll do"
        elif self.condition > 1.0 :
            return "You don't really want this..."
        elif self.condition >= 0.0 :
            return "Burn it"

class Item:
    
    def __init__(self, category = None, condition = None):
        self.category = ""
        if category:
            self.category = category
        self.condition = 0.0
        if condition:
            self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition >= 5:
            return "Bought it and forgot it. Never used."
        elif self.condition >= 4:
            return "Used a couple times. Like new."
        elif self.condition >= 3:
            return "It's time for an upgrade, but this still works"
        elif self.condition >= 2:
            return "Lovingly used"
        elif self.condition >= 1:
            return "Really really lovingly used"
        elif self.condition >= 0:
            return "Not so lovingly, but still really used"
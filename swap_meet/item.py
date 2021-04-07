class Item:
    def __init__(self, category="", condition=0, condition_description=""):
        self.category = category
        self.condition = condition

    def condition_description(self):
        if self.condition == 1:
            return "Throw away"
        elif self.condition == 2:
            return "Heavily used"
        elif self.condition == 3:
            return "Acceptable"
        elif self.condition == 4:
            return "Gently used"
        elif self.condition == 5:
            return "Almost brand new!"
        else:
            return "Mint Condition!"

    def __str__(self):
        return "Hello World!"


class Item:

    def __init__(self, condition= 0, category= ""):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition > 4:
            return "Excellent Condition!"
        elif 3 < self.condition > 4:
            return "Barely used!"
        elif 1 < self.condition > 3:
            return "Needs a little TLC"
        else:
            return "This item could use A LOT of LOVE."




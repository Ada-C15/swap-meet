class Decor:
    def __init__(self, condition=None):
        self.category = "Decor"
        if condition == None:
            self.condition = 0
        else:
            self.condition = condition

    def condition_description(self):
        if self.condition == 1:
            return "Not in the best shape, but still usable!"
        elif self.condition == 2:
            return "Has received a lot of love, and could definitely use more!"
        elif self.condition == 3:
            return "In fair condition! Definitely not the worst thing on the shelf!"
        elif self.condition == 4:
            return "Very lightly used, but not mint condition."
        elif self.condition == 5:
            return "Like new! It's your lucky day!!"

    def __str__(self):
        return "Something to decorate your space."
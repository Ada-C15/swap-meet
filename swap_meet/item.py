class Item:
    def __init__(self, category="", condition=None):
        if self.__class__ == Item or category:
            self.category = category
        else:
            self.category = self.__class__.__name__
        self.condition = condition

    def __str__(self):
        return "Hello World!"
        # # more realistic
        # return f"This is a {self.category} with condition {self.condition}"

    def condition_description(self):
        if self.condition > 4:
            return "near mint"
        elif self.condition > 3:
            return "very good"
        elif self.condition > 2:
            return "good"
        elif self.condition > 1:
            return "fair"
        else:
            return "poor"

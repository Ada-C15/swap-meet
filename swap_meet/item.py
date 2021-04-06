class Item:

    def __init__(self, category = None, condition = None):
        if category == None:
            self.category = ""
        else:
            self.category = category

        if condition == None:
            self.conditionn = 0
        else:
            self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition > 0 and self.condition <= 1:
            return "Trash"
        elif self.condition > 1 and self.condition <= 2:
            return "Slightly better than Trash"
        elif self.condition > 2 and self.condition <= 3:
            return "Average"
        elif self.condition > 3 and self.condition <= 4:
            return "Lightly Used"
        elif self.condition > 4 and self.condition <= 5:
            return "Mint Condition"
        else:
            return "Please choose a number between 1 and 5."
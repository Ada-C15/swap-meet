from .vendor import Vendor

class Item():
    def __init__(self, category = "", condition = 0.0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        self.condition = int(self.condition)

        if self.condition >= 5:
            return('New')
        elif self.condition >= 4:
            return('Excellent')
        elif self.condition >= 3:
            return('Good')
        elif self.condition >= 2:
            return('Fair')
        elif self.condition >= 1:
            return('Salvage')
        else:
            return('It should have been burned years ago, but it\'s up for sale.')

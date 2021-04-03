from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition=None):
        self.category = "Decor"
        if condition == None:
            self.condition = 0
        else:
            self.condition = float(condition)

    def condition_description(self):
        return super().condition_description()
    
    def __str__(self):
        return "Something to decorate your space."
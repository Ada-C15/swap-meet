from swap_meet.item import Item
class Decor(Item):
    def __init__(self, condition = 0):
        self.category = "Decor"
        self.condition = condition
    def __str__(self):
        return "Something to decorate your space."
    # def __init__(self):
    #     Item.__init__(self)
    #     self.category = "Decor"
    # def __str__(self):
    #     return "Something to decorate your space."
    # def condition_description(self):
    #     super().condition_description()
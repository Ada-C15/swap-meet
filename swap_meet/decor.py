from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category = "", condition = 0):
        # super().__init__(category = "Decor")
        self.category = "Decor"
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        return super().condition_description()
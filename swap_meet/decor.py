from swap_meet.item import Item
class Decor(Item):
    def __init__(self, condition = 0):
        self.category = "Decor"
        self.condition = condition
        # super().__init__("Decor", condition)
        self.description = self.condition_description()
    
    def __str__(self):
        return "Something to decorate your space."
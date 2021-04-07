from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition = 0):
        self.category = "Electronics"
        self.condition = float(condition)

    def __str__(self):
        if str(Electronics):
            return "A gadget full of buttons and secrets."



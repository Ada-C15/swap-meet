from .item import Item

class Electronics(Item):
    def __init__(self, age = None, category = "Electronics", condition = 0):
        super().__init__(age, category, condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
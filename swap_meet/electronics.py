from .item import Item


class Electronics(Item):
    def __init__(self, condition = None, age = None):
        category = "Electronics"
        super().__init__(category, condition, age)

    
    def __str__(self):
        return "A gadget full of buttons and secrets."



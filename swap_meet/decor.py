from .item import Item


class Decor(Item):
    def __init__(self, category="", condition=0, condition_description=" "):
        super().__init__("Decor", condition)

    def __str__(self):
        return "Something to decorate your space."


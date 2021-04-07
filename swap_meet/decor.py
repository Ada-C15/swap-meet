from .item import Item


class Decor(Item):
    """
    A class to represent a Decor item
    """

    def __init__(self, condition: float = 0, age: float = 0):
        super().__init__("Decor", condition, age)

    def __str__(self) -> str:
        return "Something to decorate your space."

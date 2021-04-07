from .item import Item


class Electronics(Item):
    """
    A class to represent an electronics Item
    """

    def __init__(self, condition: float = 0, age: float = 0):
        super().__init__("Electronics", condition, age)

    def __str__(self) -> str:
        return "A gadget full of buttons and secrets."


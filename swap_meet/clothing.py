from .item import Item


class Clothing(Item):
    """
    A class to represent a clothing Item
    """

    def __init__(self, condition: float = 0, age: float = 0):
        super().__init__("Clothing", condition, age)

    def __str__(self) -> str:
        return "The finest clothing you could wear."

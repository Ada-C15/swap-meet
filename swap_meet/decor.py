from .item import Item


class Decor(Item):
    """
    A class to represent a Decor item

    Attributes
    category: "Decor"
    condition: float (default is 0) on a scale of 0-5
    age: float (default is 0) in years
    """

    def __init__(self, condition: float = 0, age: float = 0):
        super().__init__("Decor", condition, age)

    def __str__(self) -> str:
        return "Something to decorate your space."

    def condition_description(self) -> str:
        return super().condition_description()

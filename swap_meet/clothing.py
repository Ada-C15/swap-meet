from .item import Item


class Clothing(Item):
    """
    A class to represent a clothing Item

    Attributes
    category: "Clothing"
    condition: float (default is 0) on a scale of 0-5
    age: float (default is 0) in years
    """

    def __init__(self, condition: float = 0, age: float = 0):
        super().__init__("Clothing", condition, age)

    def __str__(self) -> str:
        return "The finest clothing you could wear."

    def condition_description(self) -> str:
        return super().condition_description()

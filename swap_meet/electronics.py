from .item import Item


class Electronics(Item):
    """
    A class to represent an electronics Item

    Attributes
    category: "Electronics"
    condition: float (default is 0) on a scale of 0-5
    age: float (default is 0) in years
    """

    def __init__(self, condition: float = 0, age: float = 0):
        super().__init__("Electronics", condition, age)

    def __str__(self) -> str:
        return "A gadget full of buttons and secrets."

    def condition_description(self) -> str:
        return super().condition_description()

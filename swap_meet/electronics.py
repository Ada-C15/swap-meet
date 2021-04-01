from .item import Item


class Electronics(Item):
    """
    A class to represent an electronics Item

    Attributes
    category: "Electronics"
    condition: default is 0
    """

    def __init__(self, condition: float = 0):
        """
        PARAMETERS: condition defaults to 0
                    category is "Electronics"
        """
        super().__init__("Electronics", condition)

    def __str__(self) -> str:
        return "A gadget full of buttons and secrets."

    def condition_description(self) -> str:
        return super().condition_description()

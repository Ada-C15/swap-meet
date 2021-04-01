from .item import Item


class Decor(Item):
    """
    A class to represent a Decor item

    Attributes
    category: "Decor"
    condition: defaults to 0
    """

    def __init__(self, condition: float = 0):
        """
        PARAMETERS: defaults to 0
                    category is "Decor"
        """
        super().__init__("Decor", condition)

    def __str__(self) -> str:
        return "Something to decorate your space."

    def condition_description(self) -> str:
        return super().condition_description()

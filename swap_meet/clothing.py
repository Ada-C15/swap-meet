from .item import Item


class Clothing(Item):
    """
    A class to represent a clothing Item

    Attributes
    category: "Clothing"
    condition: defaults to 0
    """
    def __init__(self, condition=0):
        """
        PARAMETERS: defaults to 0
                    category is "Clothing"
        """
        super().__init__("Clothing", condition)

    def __str__(self) -> str:
        return "The finest clothing you could wear."

    def condition_description(self) -> str:
        return super().condition_description()

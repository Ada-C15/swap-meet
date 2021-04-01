from .item import Item


class Clothing(Item):
    """
    A class to represent a clothing Item

    Attributes
    category: str
    condition: int or float
    """
    def __init__(self, condition=0):
        """
        PARAMETERS: condition int or float (defaults to 0)
                    category is "Clothing"
        """
        super().__init__("Clothing", condition)

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        return super().condition_description()

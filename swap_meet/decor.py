from .item import Item


class Decor(Item):
    """
    A class to represent a Decor item

    Attributes
    category: str
    condition: int or float
    """
    def __init__(self, condition=0):
        """
        PARAMETERS: condition int or float (defaults to 0)
                    category is"Decor"
        """
        super().__init__("Decor", condition)

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        return super().condition_description()

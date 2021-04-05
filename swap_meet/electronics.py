from .item import Item


class Electronics(Item):
    """
    A class to represent an electronics Item

    Attributes
    category: str
    condition: int or float (default is 0)
    """

    def __init__(self, condition=0):
        """
        PARAMETERS: condition int or float (defaults to 0)
                    category is "Electronics"
        """
        super().__init__("Electronics", condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."

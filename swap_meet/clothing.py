from .item import Item

class Clothing(Item):
    """Class `Item`'s Child class.

    Starts with default values for `condition` and `age`.
    Initializes with a named attribute for its type, `"Clothing"`.
    """

    def __init__(self, condition=0, age=0):
        super()
        self.category = "Clothing"
        self.condition = condition
        self.age = age

    def __str__(self):
        return "The finest clothing you could wear."


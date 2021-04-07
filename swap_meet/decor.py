from .item import Item

class Decor(Item):
    """Class `Item`'s Child class.

    Starts with default values for `condition` and `age`.
    Initializes with a named attribute for its type, `"Decor"`.
    """

    def __init__(self, condition=0, age=0):
        super()
        self.category = "Decor"
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Something to decorate your space."
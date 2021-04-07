from .item import Item

class Electronics(Item):
    """Class `Item`'s Child class.

    Starts with default values for `condition` and `age`.
    Initializes with a named attribute for its type, `"Electronics"`.
    """

    def __init__(self, condition=0, age=0):
        super()
        self.category = "Electronics"
        self.condition = condition
        self.age = age

    def __str__(self):
        return "A gadget full of buttons and secrets."
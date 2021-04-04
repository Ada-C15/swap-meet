from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition = 0):
        super().__init__("Electronics", condition) # doing the same in line 3 and 4

    def __str__(self):
        self.default_str = "A gadget full of buttons and secrets."
        return self.default_str

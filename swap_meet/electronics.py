# Swap Meet
# Ada Cohort 15 - Paper
# Katrina Kimzey (she|they)
# Started April 3, 2021

from .item import Item

class Electronics(Item):
    def __init__(self, condition = 0):
        super().__init__("Electronics", condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."

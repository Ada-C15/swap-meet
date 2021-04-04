# Swap Meet
# Ada Cohort 15 - Paper
# Katrina Kimzey (she|they)
# Started April 3, 2021

from .item import Item

class Clothing(Item):
    def __init__(self, condition = 0):
        super().__init__("Clothing", condition)

    def __str__(self):
        return "The finest clothing you could wear."

# Swap Meet
# Ada Cohort 15 - Paper
# Katrina Kimzey (she|they)
# Started April 3, 2021

from .item import Item

class Decor(Item):
    def __init__(self, condition = 0, age = 0):
        super().__init__("Decor", condition, age)

    def __str__(self):
        return "Something to decorate your space."
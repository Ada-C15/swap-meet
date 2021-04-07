############### TEST WAVE 5 (5 tests) PASSED ###############
from .item import Item

### test 5.2 PASSED ###
# Has an attribute category that is "Decor"
class Decor(Item):
    def __init__(self, condition = 0):
        super().__init__("Decor", condition)

    def __str__(self):
        return "Something to decorate your space."
# stringify method returns "Something to decorate your space."
    def decor_condition_description(self, condition): 
        super().condition_description()
# All 3 classes and Item class have an attribute called condition, which can be default = 0 - rendering it optional in the initializer
# All 3 classes and Item class have an instance method:
# condition_description() describes the condition in words 
############### TEST WAVE 5 (5 tests) PASSED ###############
from .item import Item
### test 5.3 PASSED ###
# Has an attribute category that is "Electronics"
class Electronics(Item):
    def __init__(self, condition = 0):
        super().__init__("Electronics", condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
# stringify method returns "A gadget full of buttons and secrets." call it with str(instance)
    def elect_condition_description(self, condition): 
        super().condition_description()
# All 3 classes and Item class have an attribute called condition, which can be default = 0 - rendering it optional in the initializer
# All 3 classes and Item class have an instance method: condition_description() describes the condition in words 
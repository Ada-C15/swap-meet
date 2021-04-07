############### TEST WAVE 5 (5 tests) PASSED ###############
from .item import Item

### test 5.1 PASSED ###
# Has an attribute category that is "Clothing"
# these subclasses are teaching me about the default-arguments/optional
# in this subclass - the argument "category" is "Clothing" - it is constant and not variable
# Clothing is a special type of item where the category is always "Clothing"
# Need to look out for when to make attributes default/optional/variable OR constant

class Clothing(Item):
    def __init__(self, condition = 0):
        super().__init__("Clothing", condition)

    def __str__(self):
        return "The finest clothing you could wear."
#stringify method returns "The finest clothing you could wear."
    def clothing_condition_description(self, condition): 
        super().condition_description()
# All 3 classes and Item class have an attribute called condition, which can be default = 0 - rendering it optional in the initializer
# All 3 classes and Item class have an instance method: condition_description() describes the condition in words 
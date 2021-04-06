
# WAVE 5

from .item import Item

class Clothing(Item):

    def __init__(self, category = "", condition=0, age = 0): 
        super().__init__(category = "Clothing", condition = condition, age = age) 
 
    def __str__(self):
        return "The finest clothing you could wear."


































   # # the category for all instances of clothing is "clothing"
    # def __init__(self, category = "", condition=0):
    #     # self.category = "Clothing"
    #     # self.condition = condition
    #     Item.__init__(self, "Clothing", condition)


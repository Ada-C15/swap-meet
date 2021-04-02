from .item import Item

class Clothing(Item):

    def __init__(self, category = "", condition = 0): # setting a default value for the parameter
        # self.category = "Clothing"
        # self.condition = condition
    
        super().__init__(category="Clothing", condition=condition) # tells what the value is
 
    def __str__(self):
        return "The finest clothing you could wear."


































   # # the category for all instances of clothing is "clothing"
    # def __init__(self, category = "", condition=0):
    #     # self.category = "Clothing"
    #     # self.condition = condition
    #     Item.__init__(self, "Clothing", condition)


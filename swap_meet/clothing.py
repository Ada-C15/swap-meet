from swap_meet.item import Item

# For TEST 18, 21 WAVE 05 - PASSED!
class Clothing(Item): # I want it to have an attribute name
    def __init__(self, condition = 0):
        super().__init__("Clothing", condition) # doing the same in line 15 and 6
        # but super() lets me call Item __init__ function 
        # Clothing(Item) allows me to call Item's methods/functions

    def __str__(self):
        self.default_str = "The finest clothing you could wear."
        return self.default_str

#-------------------------
## Above code is similar to this - accomplishes the same for now
# class Clothing(Item):
#     def __init__(self, category = "", condition = 0):
#         self.category = "Clothing"
#         self.condition = condition

#     def __str__(self):
#         return "The finest clothing you could wear."



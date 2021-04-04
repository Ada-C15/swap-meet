from swap_meet.item import Item

class Clothing(Item): 
    def __init__(self, condition = 0):
        # super() lets me call Item __init__ function 
        super().__init__("Clothing", condition) 

    def __str__(self):
        self.default_str = "The finest clothing you could wear."
        return self.default_str

#-------------------------
## Above code is similar to this - accomplishes the same 
# class Clothing(Item):
#     def __init__(self, category = "", condition = 0):
#         self.category = "Clothing"
#         self.condition = condition

#     def __str__(self):
#         return "The finest clothing you could wear."



from swap_meet.item import Item

# For TEST 19, 21 WAVE 05 - PASSED!
class Decor(Item):
    def __init__(self, condition = 0):
        super().__init__("Decor", condition) 

    def __str__(self):
        self.default_str = "Something to decorate your space."
        return self.default_str
#________________________________________
# ## Similar to above but without super:
# class Decor(Item):
#     def __init__(self, category = "", condition = 0):
#         self.category = "Decor"
#         self.condition = condition

#     def __str__(self):
#         return "Something to decorate your space."


from swap_meet.item import Item

# For TEST 20, 21 WAVE 05 - PASSED!
class Electronics(Item):
    def __init__(self, condition = 0):
        super().__init__("Electronics", condition) # doing the same in line 3 and 4

    def __str__(self):
        self.default_str = "A gadget full of buttons and secrets."
        return self.default_str

#________________________________________
# ## Similar to above but without super:
    # def __init__(self, category = "", condition = 0):
    #     self.category = "Electronics"
    #     self.condition = condition

    # def __str__(self):
    #     return "A gadget full of buttons and secrets."

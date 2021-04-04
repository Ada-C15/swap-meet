from swap_meet.item import Item

class Clothing(Item):

    def __init__(self, condition = 0):
        self.condition = condition
        
        # these are arguments for Vendor parent class, not params
        # call a function, values to pass into function
        # default parameter values
        super().__init__(category = "Clothing", condition = condition)

    def __str__(self):
        return "The finest clothing you could wear."
    
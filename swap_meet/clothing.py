from swap_meet.item import Item

class Clothing:
    
    def __init__(self, condition = 0):
        self.category = "Clothing"
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."
    
    # def condition_description(self, value = range(0,6)):
    #     if value == range(0, 1):
    #         return "Excellent condition."
    #     elif value == range(1, 2):
    #         return "Great condition."
    #     elif value == range(2, 3):
    #         return "Used."
    #     elif value == range(3, 4):
    #         return "Moderately used."
    #     else:
    #         return "Heavily used."
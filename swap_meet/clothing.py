from .item import Item

# class Clothing(Item):
#     def __init__(self, condition = None):
#         self.category = "Clothing"
#         if condition == None:
#             self.condition = 0.0
#         else:
#             self.condition = condition

class Clothing(Item):
    def __init__(self, condition = None):
        category = "Clothing"
        super().__init__(category, condition)

# class Clothing(Item):
#     def __init__(self, category = "", condition = 0.0):
#         super().__init__(category, condition)
#         self.category = "Clothing" 
        


    
    def __str__(self):
        return "The finest clothing you could wear."
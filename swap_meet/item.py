


# create an Item class 
class Item:
    def __init__(self, category = None, condition = None):
        if category == None:
            self.category = ""
        else:
            self.category = category
        if condition == None: 
            self.condition = 0.0
        else:
            self.condition = condition


# class Item: 
#     def __init__(self, category = "", condition = 0.0):
#         self.category = category 
#         self.condition = condition


    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        pass


        




        
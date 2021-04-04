


# create an Item class 
class Item:
    def __init__(self, category = None, condition = None, age = None):
        if category == None:
            self.category = ""
        else:
            self.category = category
        if condition == None: 
            self.condition = 0.0
        else:
            self.condition = condition
        if age == None:
            self.age = 9999
        else:
            self.age = age


# class Item: 
#     def __init__(self, category = "", condition = 0.0):
#         self.category = category 
#         self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if int(self.condition) in range(0, 2):
            return "This item is in poor condition."
        elif int(self.condition) in range(2, 3):
            return "This item is in average condition."
        elif int(self.condition) in range(3 , 4):
            return "This item is in fair condition."
        elif int(self.condition) in range(4, 5):
            return "This item is in good condition."
        else:
            return "This item is in excellent condition"



        


        




        
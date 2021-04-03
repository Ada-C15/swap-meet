## I might to have the classess vendor that take an item in the 
## add and remove functions???

# For TEST 6 WAVE 02, TEST 9 - WAVE 03 - PASSED!

class Item:
    def __init__(self, category = "", condition = 0): #name,
        self.category = category
        self.condition = condition
        # self.name = name

    def __str__(self):
        self.default_str = "Hello World!"
        return self.default_str
        
    def condition_description(self):
        # condition_cat = [(0, "You probably want a glove "), (1, "Heavily used and loved"), \
        # ( 2, "Check it out!"), (3, "Giving it its' all"), (4, "Living its' best life"), (5,  "Minty!")]
        # message = "Item's Condition: "
        # for i in range(len(condition_cat)):
        #     if self.condition == condition_cat[i][0]: ## and== condition_cat[] self.category[i][0]:
        #         return message + self.category[i][1]
        #     elif self.condition == None and self.category < 0 and self.category > 5:
        #         return message + "Mixed bag of condition!"
        #     # else:
        #     #     return message + "Not sure what you are getting into"  

        condition_cat = [(0, "You probably want a glove "), (1, "Heavily used and loved"), \
        ( 2, "Check it out!"), (3, "Giving it its' all"), (4, "Living its' best life"), (5,  "Minty!")]
        message = "Item's Condition: + "
        if self.condition == None or self.condition < 0 or self.condition > 5:
            return message + "It's a mixed bag, sorry can't tell you exactly!"
        for i in range(len(condition_cat)):
            if self.condition == condition_cat[i][0]: ## and== condition_cat[] self.category[i][0]:
                return message + condition_cat[i][1]


            

        
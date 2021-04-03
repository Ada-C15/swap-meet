## I might to have the classess vendor that take an item in the 
## add and remove functions???

# For TEST 6 WAVE 02, TEST 9 - WAVE 03 - PASSED!

class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
        
    def condition_description(self):
        condition_cat.self = [(0, "You probably want a glove "), (1, "Heavily used and loved"), \
        ( 2, "Check it out!"), (3, "Giving it its' all"), (4, "Living its' best life"), (5,  "Minty!")]
        message = "Condition:"
        for rating in range(len(condition_cat.self)):
            if self.condition == self.category[i][0]:
                return message + self.category[i][1]
            elif self.condition == None and self.category < 0 and self.category > 5:
            return message + "Mixed bag of condition!"
            else:
                return message + "Not sure what you are getting into"  



            
    # - def condition_description()`, 
# Prints condition_message:
# based on category value, assuming they all range from 0 to 5. 
# Basic descriptions 5 = 'mint'
#                   4 = "living its' best life"
#                   3 = "giving its' all"
#                   2 = "check it out!"
#                     1= "heavily used and loved"
#                     0 = "You probably want a glove "
        
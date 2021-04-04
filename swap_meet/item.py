class Item:
    def __init__(self, category = "", condition = 0): 
        self.category = category
        self.condition = condition

    def __str__(self):
        self.default_str = "Hello World!"
        return self.default_str
        
    def condition_description(self): 
        condition_cat = [(0, "You probably want a glove "), (1, "Heavily used and loved"), \
        ( 2, "Check it out!"), (3, "Giving it its' all"), (4, "Living its' best life"), (5,  "Minty!")]
        message = "Item's Condition: + "
        if self.condition == None or self.condition < 0 or self.condition > 5:
            return message + "It's a mixed bag, sorry can't tell you exactly!"
        for i in range(len(condition_cat)):
            if self.condition == condition_cat[i][0]: ## and== condition_cat[] self.category[i][0]:
                return message + condition_cat[i][1]


            

        
class Item:

    def __init__(self, category = "", condition = 0, age = 0):
        if category is None:
            self.category = ""
        else:
            self.category = category
        if condition is None:
            self.condition = 0
        else:
            self.condition = condition
        if age is None:
                self.age = 0
        else:
            self.age = age

    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):

        if self.condition == 0:
            return "Poor"
        elif self.condition == 1:
            return "Fair"
        elif self.condition == 2:
            return "Good"
        elif self.condition == 3:
            return "Very good"
        elif self.condition == 4:
            return "Like new"
        elif self.condition == 5:
            return "Brand new"


    
    


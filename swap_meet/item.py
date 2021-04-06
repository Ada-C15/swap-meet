class Item: 
    def __init__(self, category="", condition=0, age=1000):
        self.category = category
        self.condition = float(condition)
        self.age = float(age)

    def __str__(self): 
        return "Hello World!"

    def condition_description(self):
        if self.condition > 4.0: 
            return "This item is beyond perfection!" 
        elif self.condition > 3.0: 
            return "You would not want to miss out on this item!"
        elif self.condition > 2.0: 
            return "This item is in good condition!"
        elif self.condition > 1.0: 
            return "This item may not be in the perfect condition, but you may need it one day!"
        else: 
            return "One person's trash might be another person's treasure!"
    
    


        
    
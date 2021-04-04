class Item: 
    def __init__(self,category='', condition= 0, age=0): 
        self.category = category
        self.condition = condition 
        self.age = age 

    def __str__(self):
        return "Hello World!"


    def condition_description(self): 
        if self.condition == 0: 
            return "Try harder"
        elif self.condition == 1: 
            return "Good job and keep going"
        elif self.condition == 2: 
            return "You are making good progress"
        elif self.condition == 3: 
            return "Almost perfection"
        elif self.condition == 4: 
            return "Excellent"
        elif self.condition == 5: 
            return "You are a rockstar"
        else:
            return "Unknown condition"

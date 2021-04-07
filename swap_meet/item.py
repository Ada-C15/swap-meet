class Item:
    #Had to add the parameter too all of the children constructors
    def __init__(self, category = "", condition = 0): # THIS IS THE INITIALIZER 
        self.category = category
        self.condition = condition
        
    def __str__(self):
        return "Hello World!"
        
    def condition_description(self): # THIS CONDITION  WILL BE PASSED TO THE CLASSES 
        if self.condition == 0:
            return 'scam'
        
        elif self.condition < 1: 
            return 'cant hurt'
        
        elif self.condition < 2: 
            return 'knock off'
        
        elif self.condition < 3: 
            return 'fair' 

        elif self.condition < 4: 
            return 'good' 

        else: 
            return 'mint' 
class Clothing:
    
    def __init__(self, category = "Clothing", condition = 0):
        
        self.category = category
        self.condition = condition 

    def __str__(self):
       
        return "The finest clothing you could wear."

    def condition_description(self):

        if self.condition == 1: 
            return "Geez, maybe put that back."
        elif self.condition == 2:
            return "Well, could be worse."
        elif self.condition == 3:
            return "What are the savings from retail value?"
        elif self.condition == 4:
            return "Almost in perfect condition"
        elif self.condition == 5:
            return "I am delighted from the sun and back"
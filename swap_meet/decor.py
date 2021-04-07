class Decor:

    def __init__(self, category = "Decor", condition = 0.0):
        
        self.category = category
        self.condition = condition 
    
    def __str__(self):
        return "Something to decorate your space."

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

class Item: 

    def __init__(self, category="", condition=0.0):

        self.category = category 
        self.condition = condition 

    def __str__(self):
        return "Hello World!"

    def condition_description(self):

        if self.condition == 1.0: 
            return "Geez, maybe put that back."
        elif self.condition == 2.0:
            return "Well, could be worse."
        elif self.condition == 3.0:
            return "What are the savings from retail value?"
        elif self.condition == 4.0:
            return "Almost in perfect condition"
        elif self.condition == 5.0:
            return "I am delighted from the sun and back"  



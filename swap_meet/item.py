

class Item:

    def __init__(self, category = None, condition = None):
        if category:
            self.category = category
        else:
            self.category = ""

        if condition:
            self.condition = float(condition)
        else:
            self.condition = 0


    def __str__(self):
        return "Hello World!"

    

    def condition_description(self):
        if self.condition > 4.0 :
            return "super duper best condition"
        elif self.condition > 3.0 :
            return "pretty alright!"
        elif self.condition > 2.0 :
            return "Has seen better days"
        elif self.condition > 1.0 :
            return "maybe wash it once you get home"
        elif self.condition >= 0.0 :
            return "pretty terrible!!!"
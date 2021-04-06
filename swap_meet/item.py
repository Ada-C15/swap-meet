class Item:
    def __init__(self, category = "", condition = 0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition >= 5.0:
            return "Better than 5G."
        elif self.condition >= 4.0:
            return "Alright alright alright."
        elif self.condition >= 3.0:
            return "Good."
        elif self.condition >= 2.0:
            return "Not bad. But not good."
        else:
            return "Bad."

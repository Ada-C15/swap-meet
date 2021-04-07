
class Item:

    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition
    
    # `Item` overrides its stringify method
    def __str__(self):
        print(super().__str__())
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "absolutely disappointing"
        elif self.condition == 1:
            return "disappointing"
        elif self.condition == 2:
            return "meeds"
        elif self.condition == 3:
            return "meeds plus"
        elif self.condition == 4:
            return "grood"
        elif self.condition == 5:
            return "dYnAmItE"
        

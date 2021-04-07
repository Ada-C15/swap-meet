#Wave 2
class Item:
    def __init__(self, category = "", condition=0,):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

#Wave 5    
    def condition_description(self):
        condition = self.condition
        if condition >= 4.0:
            return (f"The condition rating of this item is a {condition}, it's almost new")
        elif condition >= 3.0:
            return (f"The condition rating of this item is a {condition}, it's in good condition and gently used.")
        elif condition >= 2.0:
            return (f"The condition rating of this item is a {condition}, it's in fair condition and has cosmetic flaws and signs of use.")
        elif condition >= 0.0:
            return (f"The condition rating of this item is a {condition}, it's in poor condition and has some major cosmetic flaws.")
        


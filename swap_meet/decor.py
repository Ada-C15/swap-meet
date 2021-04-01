class Decor:
    def __init__(self,category = "Decor", condition = 0.0):
        self.category = category
        self.condition = float(condition)
    
    def __str__(self):
        return "Something to decorate your space."
    
    def condition_description(self):
        return f"The condition of this item is rated as a {self.condition}"
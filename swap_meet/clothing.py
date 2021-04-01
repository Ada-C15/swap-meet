class Clothing:
    def __init__(self,category = "Clothing", condition = 0.0):
        self.category = category
        self.condition = float(condition)
    
    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        return f"The condition of this item is rated as a {self.condition}"
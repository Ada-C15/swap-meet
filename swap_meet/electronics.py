class Electronics:
    def __init__(self, category = "Electronics", condition = 0.0):
        self.category = category
        self.condition = float(condition)
    
    def __str__(self):
        return "A gadget full of buttons and secrets."
    
    def condition_description(self):
        return f"The condition of this item is rated as a {self.condition}"
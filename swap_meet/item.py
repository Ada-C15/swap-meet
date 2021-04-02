class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = float(condition)
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        return f"The condition of this item is rated as a {self.condition}"


    


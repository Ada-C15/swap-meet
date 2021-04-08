class Item:
    def __init__(self, item = "Hello World!", category="", condition = 0):
        self.category = category
        self.item = item
    
    def __str__(self):
        return f"{self.item}"

    def __float__(self):
        return f"{self.condition}"

    def condition_description(self):
        return f"{self.condition}"



    

    
class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        condition_desc = ["zero", "one", "two", "three", "four", "five"]
        return condition_desc[self.condition]

        









class Item:
    def __init__(self, category = ""):
        if category == None:
            self.category = ""
        else:
            self.category = category
    
    def __str__(self):
        return "Hello World!"


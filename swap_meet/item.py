class Item:
    
    def __init__(self, category=""):
        if category == "":
            self.category = ""
        else:
            self.category = category

    def __str__(self):
         return "Hello World!"

class Item:
    
    def __init__(self, category=""):
        if not category:
            self.category = ""
        else:
            self.category = category 

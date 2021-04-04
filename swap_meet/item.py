class Item:
    def __init__(self, category = "", condition = 0.0):
        if category == None:
            self.category = ""
        else:
            self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if 0 < self.condition < 1:
            return "burn it"
        elif 1 <= self.condition < 2:
            return "I don't know about this..."
        elif 2 <= self.condition < 3:
            return "meh"
        elif 3 <= self.condition < 4:
            return "decent"
        elif 4 <= self.condition < 5:
            return "excellent"
        elif self.condition == 5:
            return "brand new"
        else:
            return None
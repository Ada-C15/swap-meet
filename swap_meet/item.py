class Item:
    def __init__(self, category = "", condition = None):
        self.category = category
        self.condition = condition
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if int(self.condition) < 1:
            return "Are you sure you want to buy this?"
        elif int(self.condition) < 2:
            return "One person's trash is another's treasure..."
        elif int(self.condition) < 3:
            return "You like a project don't you?"
        elif int(self.condition) < 4:
            return "What a find!"
        elif int(self.condition) > 4:
            return "This is practically brand new!"

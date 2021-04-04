class Item:
    def __init__(self, category=None):
        if category == None:
            self.category = ""
        else:
            self.category = category
    
    """
    This method personalizes the output for when 
    str() is called, and returns the provided message.
    """
    def __str__(self):
        return "Hello World!"
    
    """
    This method returns a condition description depending
    on the value of that specific item's condition.
    """
    def condition_description(self):
        if 1.0 > self.condition >= 0.0:
            return "Not in the best shape, but still usable!"
        elif 2.0 > self.condition >= 1.0:
            return "Has received a lot of love, and could definitely use more!"
        elif 3.0 > self.condition >= 2.0:
            return "In fair condition! Definitely not the worst thing on the shelf!"
        elif 4.0 > self.condition >= 3.0:
            return "Very lightly used, but not mint condition."
        elif 5.0 >= self.condition >= 4.0:
            return "Like new! It's your lucky day!!"
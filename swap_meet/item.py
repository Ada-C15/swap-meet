class Item():
    
    def __init__(self, category = "", condition = 0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
    
            if self.condition == 0:
                return "This is gross.  Why do you still have it?"
            elif self.condition == 1:
                return "The item is in pretty rough condition."
            elif self.condition == 2:
                return "Below average."
            elif self.condition == 3:
                return "Gently used."
            elif self.condition == 4:
                return "Great condition, minimal flaws."
            elif self.condition == 5:
                return "Mint condition/like new!"




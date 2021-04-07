class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "This should have been recycled."
        elif self.condition == 1:
            return "This is really bad."
        elif self.condition == 2:
            return "This is in somewhat okay condition."
        elif self.condition == 3:
            return "This is in decent condition."
        elif self.condition == 4:
            return "This almost looks new!"
        elif self.condition == 5:
            return "This looks so new! Very nice."
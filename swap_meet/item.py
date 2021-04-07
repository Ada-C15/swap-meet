class Item:

    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition in range(0, 1):
            return "Excellent condition."
        elif self.condition in range(1, 2):
            return "Great condition."
        elif self.condition in range(2, 3):
            return "Used."
        elif self.condition in range(3, 4):
            return "Moderately used."
        elif self.condition == 5:
            return "Heavily used."

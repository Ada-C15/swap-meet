class Item:

    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self, value = range(0,6)):
        if value == range(0, 1):
            return "Excellent condition."
        elif value == range(1, 2):
            return "Great condition."
        elif value == range(2, 3):
            return "Used."
        elif value == range(3, 4):
            return "Moderately used."
        elif value == 5:
            return "Heavily used."

class Item:

    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    # def stringified_item(self):
    #     str(self) return "Hello World!"

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5.0:
            return "Brand new"
        elif 4.0 <= self.condition < 5.0:
            return "Excellent condition"
        elif 3.0 <= self.condition < 4.0:
            return "Good condition"
        elif 2.0 <= self.condition < 3.0:
            return "Fair condition"
        elif 1.0 <= self.condition < 2.0:
            return "Bad condition"
        elif self.condition < 1.0:
            return "Time to recycle"

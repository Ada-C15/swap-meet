class Item:
    def __init__(self, category='', condition=0):
        self.category = category
        if isinstance(condition, float) or isinstance(condition, int):
            self.condition = condition
        else:
            raise Exception("A condition is not a number.")

    def __str__(self):
        return "Hello World!"
        # return self.category

    def condition_description(self):
        description = ""
        if 0.0 <= self.condition < 1.0:
            description = "Seems uselesss, unless ..."
        elif 1.0 <= self.condition < 2.0:
            description = "Happy if you can give it a try!"
        elif 2 <= self.condition < 3.0:
            description = "Used - Fair"
        elif 3 <= self.condition < 4.0:
            description = "Used - Good"
        elif 4 <= self.condition < 5.0:
            description = "Used - Like new"
        else:
            description = "Brand New"
        return description

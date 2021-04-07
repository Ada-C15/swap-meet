class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition <= 0:
            return "is not good"
        elif self.condition < 3:
            return "is still good"
        else:
            return "is pretty much new"
            

    
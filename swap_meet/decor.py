class Decor:

    def __init__(self, condition = None):
        self.category = "Decor"
        self.condition = 3.5

    def __str__(self):
        return "Something to decorate your space."
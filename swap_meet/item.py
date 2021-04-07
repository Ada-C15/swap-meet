class Item:
    def __init__(self, category = "", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition < 1:
            return "I would be cautious handling this, it's really old."
        elif self.condition < 2:
            return "Probably has some use still left?"
        elif self.condition < 3:
            return "Doesn't look like much but it will get the job done."
        elif self.condition < 4:
            return "This has a lot of use left!"
        elif self.condition < 5:
            return "Really good condition!"
        else:
            return "It's perfect, never used, still in orginal packaging."

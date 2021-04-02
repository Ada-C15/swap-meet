from .item import Item

class Decor(Item):
    def __init__(self, condition=0):
        self.category = "Decor"
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        return super().condition_description()
        # if 4 < self.condition <= 5:
        #     # print(self.condition, "mint condition")
        #     return "mint condition"
        # elif 3 < self.condition <= 4:
        #     # print(self.condition, "kind of worth it")
        #     return "kind of worth it"
        # elif 0 <= self.condition <= 3:
        #     # print(self.condition, "you get what you pay for")
        #     return "you get what you pay for"

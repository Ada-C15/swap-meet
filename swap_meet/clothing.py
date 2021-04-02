from .item import Item

class Clothing(Item):
    def __init__(self, condition=0):
        self.category = "Clothing"
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        # print(super().condition_description())
        # print(type(super().condition_description()))
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
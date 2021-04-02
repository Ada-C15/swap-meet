class Item:
    def __init__(self, category=None, condition=0):
        if category is None:
            category = ""
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if 4 < self.condition <= 5:
            # print(self.condition, "mint condition")
            return "mint condition"
        elif 3 < self.condition <= 4:
            # print(self.condition, "kind of worth it")
            return "kind of worth it"
        elif 0 <= self.condition <= 3:
            # print(self.condition, "you get what you pay for")
            return "you get what you pay for"
class Item:
    def __init__(self, category=None, condition=0, age=None):
        if category is None:
            category = ""
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if 4 < self.condition <= 5:
            return "mint condition"
        elif 3 < self.condition <= 4:
            return "kind of worth it"
        elif 0 <= self.condition <= 3:
            return "you get what you pay for"
class Item:
    def __init__(self, category="", condition=0.0):
        if category == "":
            self.category = ""
        else:
            self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition < 0:
            return "You're being rude. "
        elif 0.0 <= self.condition <= 1.0:
            return "This item is honestly no good, but it may inspire you to create your own... "
        elif 1.1 <= self.condition <= 2.0:
            return "Extremely heavily used. Extremely. "
        elif 2.1 <= self.condition <= 3.0:
            return "Good, not great. "
        elif 3.1 <= self.condition <= 4.0:
            return "Only gently used! This should last you a while. "
        elif 4.1 <= self.condition <= 5.0:
            return "This is in mint condition! What a find! "
        elif self.condition > 5.0:
            return "Good for you, but we don't score above 5.0 here. "
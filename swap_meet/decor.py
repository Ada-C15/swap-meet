class Decor:
    
    def __init__(self, condition=None):
        self.category = "Decor"
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        if self.condition <= 1:
            return "This is in terrible condition"
        elif 1 < self.condition <= 2:
            return "This is in poor condition"
        elif 2 < self.condition <= 3:
            return "This is in okay condition"
        elif 3 < self.condition <= 4:
            return "This is in good condition!"
        else:
            return "This is in excellent condition!"
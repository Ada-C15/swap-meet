class Electronics:
    def __init__(self, condition = None, category = "Electronics"):
        self.condition = condition
        self.category = category

    def __str__(self):
        return "A gadget full of buttons and secrets."

    def condition_description(self):
        return str(self.condition)
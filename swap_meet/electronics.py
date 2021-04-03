from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition=None):
        self.category = "Electronics"
        if condition == None:
            self.condition = 0
        else:
            self.condition = float(condition)

    def condition_description(self):
        return super().condition_description()

    def __str__(self):
        return f"A gadget full of buttons and secrets."
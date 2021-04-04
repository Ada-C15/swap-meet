from swap_meet.item import Item


class Electronics(Item):

    def __init__(self, category="Electronics", condition=0):
        super().__init__(category, condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."

    def condition_description(self):
        
        if self.condition == 5:
            return "New/Unused"
        elif self.condition == 4:
            return "Like New"
        elif self.condition == 3:
            return "Used/Average"
        elif self.condition == 2:
            return "Very Used"
        elif self.condition == 1:
            return "Yikes"
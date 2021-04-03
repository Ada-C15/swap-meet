from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category = "Clothing", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."

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
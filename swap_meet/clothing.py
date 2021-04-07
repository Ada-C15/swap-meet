from swap_meet.item import Item


class Clothing(Item):

    def __init__(self):
        self.category = "Clothing"

    def __str__(self):
        return "The finest clothing you could wear."

    def condition(self):
        if  self.condition == None:
            self.condition = 0
        else:
            self.condition = condition

    def condition_description(self):
        if self.value == 0:
            return "This should have been recycled."
        elif self.value == 1:
            return "It almost looks like a rag."
        elif self.value == 2:
            return "This is in somewhat okay condition."
        elif self.value == 3:
            return "This is in decent condition."
        elif self.value == 4:
            return "This almost looks new!"
        elif self.value == 5:
            return "This looks so new! Very nice."
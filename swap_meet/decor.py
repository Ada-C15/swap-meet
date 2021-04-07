from swap_meet.item import Item

class Decor(Item):

    def __init__(self):
        self.category = "Decor"

    def __str__(self):
        return "Something to decorate your space."

    def condition(self, value = None):
        if value == None:
            self.value = 0
        else:
            self.value = value

    def condition_description(self):
        if self.value == 0:
            return "This should have been recycled."
        elif self.value == 1:
            return "I don't think anyone can use this."
        elif self.value == 2:
            return "This is in somewhat okay condition."
        elif self.value == 3:
            return "This is in decent condition."
        elif self.value == 4:
            return "This almost looks new!"
        elif self.value == 5:
            return "This looks so new! Very nice."
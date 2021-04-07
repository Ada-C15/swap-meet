from swap_meet.item import Item

class Electronics(Item):

    def __init__(self):
        self.category = "Electronics"

    def __str__(self):
        return "A gadget full of buttons and secrets."

    def condition(self, value = None):
        if value == None:
            self.value = 0
        else:
            self.value = value

    def condition_description(self):
        if self.value == 0:
            return "This should have been recycled."
        elif self.value == 1:
            return "This doesn't even charge."
        elif self.value == 2:
            return "It'll work if you smack it on top."
        elif self.value == 3:
            return "This is in decent condition."
        elif self.value == 4:
            return "This almost looks new!"
        elif self.value == 5:
            return "This looks so new! Very nice."
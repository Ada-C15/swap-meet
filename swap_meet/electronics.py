#Wave 5

from swap_meet.item import Item

class Electronics(Item):

    def __init__(self, condition=0):
        Item.__init__(self, "Electronics", condition=condition)

    def __str__(self):
        return "A gadget full of buttons and secrets."
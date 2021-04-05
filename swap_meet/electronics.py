from swap_meet.item import Item

#wave 5
class Electronics(Item):
    def __init__(self):
        super().__init__("Electronics")
    
    def __str__(self):
        return "A gadget full of buttons and secrets."



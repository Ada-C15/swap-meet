from swap_meet.item import Item

# ---- Wave 5 ----- #
class Electronics(Item):
    def __init__(self, category="", condition=0): 
        self.category = "Electronics"
        self.condition = condition

    def __str__(self): 
        return "A gadget full of buttons and secrets."
    
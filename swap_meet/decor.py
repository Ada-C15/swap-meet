from swap_meet.item import Item
from swap_meet.vendor import Vendor


class Decor(Item):
    
    def __init__(self,category="",condition=None):
        self.category="Decor"
        self.condition=condition

    def __str__(self):
        return "Something to decorate your space."

         
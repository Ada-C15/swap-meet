
# WAVE 5

from .item import Item

class Electronics(Item):

    def __init__(self, category = "", condition = 0): 
        super().__init__(category="Electronics", condition=condition) 

    
    def __str__(self):
        return "A gadget full of buttons and secrets."


































    # def __init__(self):
    #     Item.__init__(self, "Electronics")


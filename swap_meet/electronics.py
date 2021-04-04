from .item import Item

class Electronics(Item):

    def __init__(self, condition = 0):

        super().__init__("Electronics", condition)

    def __str__(self) -> str:
        return "A gadget full of buttons and secrets."  

    def condition_description(self):
        return super().condition_description()

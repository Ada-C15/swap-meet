from .item import Item


class Clothing(Item):
    def __init__(self, condition = 0):
        super().__init__("Clothing", condition)

    def __str__(self) -> str:
        return "The finest clothing you could wear."     

    def condition_description(self):
        return super().condition_description()

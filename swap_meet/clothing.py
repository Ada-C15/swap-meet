from swap_meet.item import Item
class Clothing(Item):

    def __init__(self, category="", condition=0):
        self.category = "Clothing"
        self.condition = condition
        # refactor with super()

    def __str__(self):
        return "The finest clothing you could wear."

from swap_meet.item import Item
class Decor(Item):
    def __init__(self,category = "", condition = 0):
        super().__init__("Decor", condition)

    # def __init__(self,condition):
    #     super().__init__("Decor", condition = 0.0)
    #     self.category = "Decor"

    def __str__(self):
        return "Something to decorate your space."

    # def __repr__(self):
    #     return "Item('{}')".format(self.category)
    
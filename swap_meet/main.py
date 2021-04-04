class Item:
    def __init__(self, category="", condition = 0):
        self.category = category
        self.condition = float(condition)

    # def __str__(self):
    #     if str(Item):
    #         return "Hello World!"

class Electronics(Item):
    def __init__(self, condition = 0):
        self.category = "Electronics"
        self.condition = float(condition)

    # def __str__(self):
    #     if str(Electronics):
    #         return "A gadget full of buttons and secrets."





item = Item("thing", 5)
# print(item.category)
# print(item.condition)
# print(item)
electronic = Electronics(5)
print(electronic.condition)

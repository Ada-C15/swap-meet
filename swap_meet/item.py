class Item:
    def __init__(self, category = ""):
        self.category = category
    def __str__(self):
         return 'Hello World!'
    # def __repr__(self):''
    #     return "Item('{}')".format(self.category)
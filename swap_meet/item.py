
# from swap_meet.vendor import Vendor

# ***WAVE 1***


class Item:
    def __init__(self, category=None):
        self.category = category
        if category == None:
            self.category = ""
        else:
            self.category = category

# ***WAVE 3***

    def __str__(self):
        return "Hello World!"

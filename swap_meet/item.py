
from swap_meet.vendor import Vendor


class Item:
    def __init__(self, category=None):
        self.category = category
        if category == None:
            self.category = ""
        else:
            self.category = category

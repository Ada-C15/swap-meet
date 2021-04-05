import pytest
from swap_meet.vendor import Vendor
# from swap_meet.item import Item


class Item:
    def __init__(self, category=None):
        if self.category == None:
            self.category = ""
        else:
            self.category = category

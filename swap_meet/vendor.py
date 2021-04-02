from .item import Item


class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory or []
        
        # if inventory == None:
        #     self.inventory = []
        # else:
        #     self.inventory = inventory
        
        # self.inventory = inventory
        # if self.inventory is None:
        #     self.inventory = []
  
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, other_vendor, item_x, item_y):
        if item_x not in self.inventory or item_y not in other_vendor.inventory:
            return False
        item_being_swapped = self.remove(item_x)
        other_vendor.add(item_being_swapped)
        item_being_swapped = other_vendor.remove(item_y)
        self.add(item_being_swapped)
        return True


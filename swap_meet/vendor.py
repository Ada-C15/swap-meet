from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, item):
        result = self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            result = self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, other_vendor, vendor_item, other_vendor_item):
        if vendor_item not in self.inventory or other_vendor_item not in other_vendor.inventory:
            return False
        else:
            for item in other_vendor.inventory:
                if item == other_vendor_item:
                    self.inventory.append(item)
                    other_vendor.inventory.remove(item)
            for item in self.inventory:
                if item == vendor_item:
                    other_vendor.inventory.append(item)
                    self.inventory.remove(item)
            return True

    def swap_first_item(self, other_vendor):
        # first vendor is self.inventory
        # second vendor is other_vendor.inventory
        # You could potentially use super here or call the 
        # swap_items method because it is similar?
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            for item in self.inventory:
                if item == self.inventory[0]:
                    other_vendor.inventory.append(item)
                    self.inventory.remove(item)
            for item in other_vendor.inventory:
                if item == other_vendor.inventory[0]:
                    self.inventory.append(item)
                    other_vendor.inventory.remove(item)
            return True
class Vendor:
    pass
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory= []
        else:
            self.inventory = inventory
    def add(self, add_item):
        self.inventory.append(add_item)
        return add_item
    def remove(self, remove_item):
        if remove_item not in self.inventory:
            return False
        else:
            self.inventory.remove(remove_item)
            return remove_item
    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if category == item.category:
                item_list.append(item)
        return item_list
    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            vendor.add(my_item)
            vendor.remove(their_item)
            self.add(their_item)
            return True
    def swap_first_item(self, vendor_list):
        if len(self.inventory) > 0 and len(vendor_list.inventory) > 0:
            my_first_item = self.inventory [0]
            their_first_item = vendor_list.inventory[0]
            self.inventory.remove(my_first_item)
            self.inventory.insert(0, their_first_item)
            vendor_list.inventory.remove(their_first_item)
            vendor_list.inventory.insert(0,my_first_item)
            return True
        else:
            return False
    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if len(items) == 0:
            return None
        best_by_category = items[0]
        for item in items:
            if item.condition > best_by_category.condition:
                best_by_category = item
        return best_by_category
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        if my_item and their_item:
            other.inventory.remove(their_item)
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            other.inventory.append(my_item)
            return True
        else:
            return False



class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return new_item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.category == category:
                result.append(item)
        return result

    def swap_items(self, other_vendor, my_item, other_item):
        if my_item not in self.inventory or other_item not in other_vendor.inventory:
            return False
        else:
            other_vendor.inventory.append(my_item)
            self.inventory.remove(my_item)
            self.inventory.append(other_item)
            other_vendor.inventory.remove(other_item)
            return True
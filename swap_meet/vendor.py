class Vendor():
    def __init__(self, inventory = None):
        if inventory == None:
            inventory = []
        self.inventory = inventory
    
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            item = False
        return item
    
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        return items_in_category
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.append(their_item)
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.remove(their_item)
            return True
        else:
            return False
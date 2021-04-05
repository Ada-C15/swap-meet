class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else: 
            self.inventory = inventory

    def add(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category): 
        items_by_category = []
        for item in self.inventory:
            if item.category == category:
                items_by_category.append(item)
        return items_by_category
    
    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            self.add(their_item)
            vendor.remove(their_item)
            vendor.add(my_item)
            return True
        return False
    
    def swap_first_item(self, vendor):
        if len(self.inventory) and len(vendor.inventory) > 0:
            self.add(vendor.inventory[0])
            vendor.add(self.inventory[0])
            self.remove(self.inventory[0])
            vendor.remove(vendor.inventory[0])
            return True
        return False
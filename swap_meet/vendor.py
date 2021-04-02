from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None): 
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

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
    
    def swap_items(self, vendor, item_1, item_2):
        if item_1 not in self.inventory or item_2 not in vendor.inventory:
            return False
        
        found = False
        for item in self.inventory:
            if item == item_1:
                self.inventory.remove(item)
                vendor.inventory.append(item)
                found = True

        if not found:
            return False

        found = False
        for item in vendor.inventory:
            if item == item_2:
                vendor.inventory.remove(item)
                self.inventory.append(item)
                found = True
        
        return found

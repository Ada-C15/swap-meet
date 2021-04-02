class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory
        
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item 
        
        
    def remove(self, removed_item):
        for i in self.inventory:
            if i is removed_item:
                self.inventory.remove(removed_item)
                return removed_item
        return False
class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item 
        
        
    def remove(self, removed_item):
        for inventory_item in self.inventory:
            if inventory_item is removed_item:
                self.inventory.remove(removed_item)
                return removed_item
        return False

    def get_by_category(self, category = ""):
        items = []
        for inventory_item in self.inventory:
            if(inventory_item.category is category):
                items.append(inventory_item)
        return items

            
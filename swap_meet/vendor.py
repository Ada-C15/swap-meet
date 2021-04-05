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


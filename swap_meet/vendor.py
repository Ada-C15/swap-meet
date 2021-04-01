class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, item):
        self.item = item
        self.inventory.append(self.item)
        return self.item
    
    def remove(self, item):
        self.item = item
        if self.item in self.inventory:
            self.inventory.remove(self.item)
            return self.item
        else:
            return False
    
    def get_by_category(self, category = ""):
        item_list = []
        for item in self.inventory:
            if category == item.category:
                item_list.append(item)
        return item_list





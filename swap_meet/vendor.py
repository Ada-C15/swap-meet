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



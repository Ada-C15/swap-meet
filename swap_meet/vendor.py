from swap_meet.item import Item

class Vendor: 
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, remove_item):
        if remove_item not in self.inventory:
            return False
        else:
            self.inventory.remove(remove_item)
            return remove_item
    
    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list
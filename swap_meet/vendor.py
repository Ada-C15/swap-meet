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
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item

#Wave 2
    def get_by_category(self, category):
        list_of_items_in_category = []
        for item in self.inventory:
            if category == item.category:
                list_of_items_in_category.append(item)
        return list_of_items_in_category

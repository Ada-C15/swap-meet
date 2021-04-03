class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
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
        category_items = []
        for specific_item in self.inventory:
            category_items.append(specific_item)

        return category_items
    
    def swap_items(self, vendor, my_item, their_item):
        #self.vendor = vendor
        #self.my_item = item.my_item
        #self.their_item = item.their_item


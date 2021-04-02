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
    #be careful of functions returning more than one type. 

    def get_by_category(self, category):
        categorized_items =[]
        for item in self.inventory:
            if item.category is category:
                categorized_items.append(item)
        return categorized_items

    def swap_items(self, vendor, my_item, their_item):
        if their_item in vendor.inventory and my_item in self.inventory:
            self.remove(my_item)
            vendor.remove(their_item)
            self.add(their_item)
            vendor.add(my_item)
            return True
        else:
            return False
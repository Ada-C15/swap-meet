class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []      
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, vendor, my_item, their_item):
        contains_item = False

        if my_item not in self.inventory or their_item not in vendor.inventory:
            return contains_item

        for item in self.inventory:
            if item == my_item:
                self.inventory.remove(item)
                vendor.inventory.append(item)
                contains_item = True
        
        for item in vendor.inventory:
            if item == their_item:
                vendor.inventory.remove(item)
                self.inventory.append(item)
                contains_item = True
        
        return contains_item


    def swap_first_item(self, vendor):
        contains_item = False
        if not self.inventory or not vendor.inventory:
            return contains_item
        else:
            contains_item = True
        
        my_first_item = self.inventory[0]
        self.inventory.remove(my_first_item)
        vendor.inventory.append(my_first_item)

        their_first_item = vendor.inventory[0]
        vendor.inventory.remove(their_first_item)
        self.inventory.append(their_first_item)

        return contains_item

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
        else:
            contains_item = True

        if my_item in self.inventory:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)

        if their_item in vendor.inventory:
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
        
        return contains_item


    def swap_first_item(self, vendor):
        contains_item = self.check_for_empty_list(vendor)
        if not contains_item:
            return contains_item
        
        my_first_item = self.inventory[0]
        self.inventory.remove(my_first_item)
        vendor.inventory.append(my_first_item)

        their_first_item = vendor.inventory[0]
        vendor.inventory.remove(their_first_item)
        self.inventory.append(their_first_item)

        return contains_item


    def get_best_by_category(self, type, other_list=None):
        best_cond = 0
        highest_cat = None
        inventory_list = self.inventory

        if other_list != None:
            inventory_list = other_list

        for item in inventory_list:
            if item.category == type:
                if best_cond < item.condition:
                    best_cond = item.condition
                    highest_cat = item

        return highest_cat

    def check_for_empty_list(self, other_list):
        empty_list = False
        if not self.inventory or not other_list.inventory:
            return empty_list
        else:
            empty_list = True
        return empty_list

    def swap_best_by_category(self, other, my_priority, their_priority):
        contains_item = self.check_for_empty_list(other)
        if not contains_item:
            return contains_item

        highest_cat = None
        for item in self.inventory:
            if item.category == their_priority:
                highest_cat = self.get_best_by_category(item.category)
                contains_item = True
        self.inventory.remove(highest_cat)
        other.inventory.append(highest_cat)

        for item in other.inventory:
            if item.category == my_priority:
                highest_cat = self.get_best_by_category(item.category, other.inventory)
                contains_item = True
        other.inventory.remove(highest_cat)
        self.inventory.append(highest_cat)

        return contains_item

    def swap_by_newest(self, other, my_priority, their_priority):
        contains_item = self.check_for_empty_list(other)
        if not contains_item:
            return contains_item

        for item in self.inventory:
            if item.category == their_priority and item.age == "New":
                self.inventory.remove(item)
                other.inventory.append(item)
                contains_item = True

        for item in other.inventory:
            if item.category == my_priority and item.age == "New":
                other.inventory.remove(item)
                self.inventory.append(item)
                contains_item = True

        return contains_item

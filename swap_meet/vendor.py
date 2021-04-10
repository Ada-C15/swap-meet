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

        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)

            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            contains_item = True
        
        return contains_item


    def swap_first_item(self, vendor):
        contains_item = False
        if not self.inventory or not vendor.inventory:
            return contains_item

        # if not self.inventory or not vendor.inventory:
        #     return contains_item
        # else:
        #     contains_item = self.swap_items(vendor, self.inventory[0], vendor.inventory[0])

        return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])


    def get_best_by_category(self, type, other_list=None):
        inventory_list = self.inventory
        
        if other_list is not None:
            inventory_list = other_list

        best_condition = 0
        highest_category = None

        for item in inventory_list:
            if item.category == type:
                if best_condition < item.condition:
                    best_condition = item.condition
                    highest_category = item

        return highest_category

    def swap_best_by_category(self, other, my_priority, their_priority):
        contains_item = False
        
        my_item = self.get_best_by_category(their_priority, self.inventory)
        their_item = self.get_best_by_category(my_priority, other.inventory)

        contains_item = self.swap_items(other, my_item, their_item)

        return contains_item

    def swap_by_newest(self, other, my_priority, their_priority):
        contains_item = False
        if not self.inventory or not other.inventory:
            return contains_item

        
        my_newest_age = 10
        for item in self.inventory:
            if item.age < my_newest_age:
                my_newest_age = item.age

        my_item = None
        for item in self.inventory:
            if item.category == their_priority and item.age == my_newest_age :
                my_item = item

        
        their_newest_age = 10
        for item in self.inventory:
            if item.age < their_newest_age:
                their_newest_age = item.age

        their_item = None
        for item in other.inventory:
            if item.category == my_priority:
                their_item = item

        contains_item = self.swap_items(other, my_item, their_item)

        return contains_item

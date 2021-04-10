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
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)

            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        
        return False


    def swap_first_item(self, vendor):
        if self.inventory and vendor.inventory:
            return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])

        return False


    def get_best_by_category(self, type):
        best_condition = 0
        highest_category = None

        for item in self.inventory:
            if item.category == type:
                if best_condition < item.condition:
                    best_condition = item.condition
                    highest_category = item

        return highest_category

    def swap_best_by_category(self, other, my_priority, their_priority):        
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_item, their_item)

    def swap_by_newest(self, other, my_priority, their_priority):
        if not self.inventory or not other.inventory:
            return False
 
        my_newest_age = self.inventory[0].age
        my_item = self.inventory[0]
        for item in self.inventory:
            if item.age < my_newest_age:
                my_newest_age = item.age
                my_item = item

        
        their_newest_age = other.inventory[0].age
        their_item = other.inventory[0]
        for item in other.inventory:
            if item.age < their_newest_age:
                their_newest_age = item.age
                my_item = item

        return self.swap_items(other, my_item, their_item)

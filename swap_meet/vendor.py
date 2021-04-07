from .item import Item

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
        
        matching_category_list = []

        for item in self.inventory:
            if item.category == category:
                matching_category_list.append(item)
        
        return matching_category_list

    def swap_items(self, vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        self.remove(my_item)
        vendor.add(my_item)

        vendor.remove(their_item)
        self.add(their_item)

        return True

    def swap_first_item(self, vendor):

        if not self.inventory or not vendor.inventory:
            return False

        self.swap_items(vendor, self.inventory[0], vendor.inventory[0])

        return True

    def get_best_by_category(self, category):

        if not self.get_by_category(category):
            return None

        condition_tracker = 0
        best_item = 0

        for item in self.get_by_category(category):
            if item.condition > condition_tracker:
                condition_tracker = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):

        if not self.get_best_by_category(their_priority) or not other.get_best_by_category(my_priority):
            return False

        return self.swap_items(other, self.get_best_by_category(their_priority), other.get_best_by_category(my_priority))

    # Optional Enhancement attempt
    def swap_by_newest(self, vendor, my_priority, their_priority):

        if not self.get_by_category(their_priority) or not vendor.get_by_category(my_priority):
            return False

        my_item_age_tracker = self.get_by_category(their_priority)[0].age
        my_newest_item = self.get_by_category(their_priority)[0]

        for item in self.get_by_category(their_priority):
            if item.age < my_item_age_tracker:
                my_item_age_tracker = item.age
                my_newest_item = item
        
        their_item_age_tracker = vendor.get_by_category(my_priority)[0].age
        their_newest_item = vendor.get_by_category(my_priority)[0]

        for item in vendor.get_by_category(my_priority):
            if item.age < their_item_age_tracker:
                their_item_age_tracker = item.age
                their_newest_item = item
        
        return self.swap_items(vendor, my_newest_item, their_newest_item)
        

            


        





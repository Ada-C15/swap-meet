
# WAVE 1

class Vendor:

    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def __str__(self):
        return ""

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item


# WAVE 2

    def get_by_category(self, category):
        # returns a list of all items in the inventory with the specified category 
        items_list = []
        for item in self.inventory:
            if item.category == category:
                items_list.append(item)
        return items_list


# WAVE 3
    
    def swap_items(self, vendor, my_item, their_item):
        # swaps the two specified items between two vendors
        if my_item in self.inventory and their_item in vendor.inventory:
            vendor.inventory.append(my_item) 
            self.inventory.remove(my_item) 
            self.inventory.append(their_item) 
            vendor.inventory.remove(their_item) 
            return True
        else:
            return False


# WAVE 4
    
    def swap_first_item(self, vendor):
        # swaps the first item in each vendor's inventory with the specified other vendor
        if len(self.inventory) != 0 and len(vendor.inventory) != 0:
            self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
            return True
        else:
            return False
    

# WAVE 6

    def get_best_by_category(self, category):
        # returns item in best condition within the specified category
        if len(self.inventory) == 0:
            return None
        else:
            items_in_category = self.get_by_category(category)
            max_condition = 0
            max_item = None
            for item in items_in_category:
                if item.condition > max_condition:
                    max_condition = item.condition
                    max_item = item
            return max_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        # swaps items in best condition within each vendor's favorite categories between the vendors 
        if len(other.get_by_category(my_priority)) == 0 \
            or len(self.get_by_category(their_priority)) == 0:
            return False
        else:
            my_priority_best = other.get_best_by_category(my_priority)
            their_priority_best = self.get_best_by_category(their_priority)
            self.swap_items(other, their_priority_best, my_priority_best)
            return True
        

             

      
 







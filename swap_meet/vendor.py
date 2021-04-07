
# WAVE 1

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


# WAVE 2

    def get_by_category(self, category):
        # returns a list of all items in the inventory with the specified category 
        items_list = [item for item in self.inventory if item.category == category]
        return items_list

# WAVE 3
    
    def swap_items(self, vendor, my_item, their_item):
        # swaps the two specified items between two vendors
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            vendor.add(my_item) 
            self.remove(my_item) 
            self.add(their_item) 
            vendor.remove(their_item) 
            return True

# WAVE 4
    
    def swap_first_item(self, vendor):
        # swaps the first item in each vendor's inventory with the other's
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        else:
            self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
            return True    

# WAVE 6

    def get_best_by_category(self, category):
        # returns item in best condition within the specified category
        items_in_category = self.get_by_category(category)
        if items_in_category == []:
            return None
        else:
            best_condition_item = items_in_category[0]
            for item in items_in_category:
                if item.condition > best_condition_item.condition:
                    best_condition_item = item
            return best_condition_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        # swaps items in best condition within each vendor's favorite categories between the vendors 
        their_priority_best = self.get_best_by_category(their_priority)
        my_priority_best = other.get_best_by_category(my_priority)

        if their_priority_best == None or my_priority_best  == None:
            return False
        else:
            self.swap_items(other, their_priority_best, my_priority_best)
            return True


# OPTIONAL
# It makes the most sense to me to swap newest by favorite category

    def get_newest_by_category(self, category):
        # returns newest item within the specified category
        items_in_category = self.get_by_category(category)
        if items_in_category == []:
            return None
        else:
            newest_item_cat = items_in_category[0]
            for item in items_in_category:
                if item.age < newest_item_cat.age:
                    newest_item_cat = item
            return newest_item_cat

    def swap_newest_by_category(self, other, my_priority, their_priority):
        # swaps newest items within each vendor's favorite categories between them 
        their_priority_best = self.get_newest_by_category(their_priority)
        my_priority_best = other.get_newest_by_category(my_priority)

        if their_priority_best == None or my_priority_best  == None:
            return False
        else:
            self.swap_items(other, their_priority_best, my_priority_best)
            return True
        

             

      
 







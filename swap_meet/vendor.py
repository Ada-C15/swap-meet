from swap_meet.item import Item
from swap_meet.electronics import Electronics
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor


class Vendor:

    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self,item_name):
        self.inventory.append(item_name)
        return item_name

    def remove(self,item_name):
        if item_name in self.inventory:
            self.inventory.remove(item_name)
        else:
            return False
        return item_name
# Cd in terminal up 1 folder then run the specific 
# file w/ python3 -m swap_meet.vendor
    def get_by_category(self, category):
        category_list = []
        for items in self.inventory:
            print(items.category)
            if items.category == category:
                category_list.append(items)
        return category_list

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            # remove my item and give it to them
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            # remove their item and add to me
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False

    def swap_first_item(self, other_vendor):
        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0:
            # remove my first item and add to other vendor
            other_vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            # remove their first item and add to my invent. 
            self.inventory.append(other_vendor.inventory[0])
            other_vendor.inventory.remove(other_vendor.inventory[0])
            return True
        else:
            return False

    def get_best_by_category(self, category):
        if len(self.inventory) == 0:
            return None
        # Make a container for items that match category
        category_finds = []
        # loop thru invent to find matches and add to list
        
        for item in self.inventory:
            if item.category == category:
                category_finds.append(item)
        if len(category_finds) < 1:
            return None
        
        # compare ratings in finds list
        best_so_far = category_finds[0]
        if best_so_far.condition == 5:
            return best_so_far
        
        for item in category_finds[1:]:
            if item.condition > best_so_far.condition:
                best_so_far = item
                if best_so_far.condition == 5:
                    return best_so_far
        return best_so_far

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        # print(my_best.condition, my_best.category, their_best.condition, their_best.category)

        if my_best != None and their_best != None:
            other.inventory.append(my_best)
            self.inventory.remove(my_best)

            self.inventory.append(their_best)
            other.inventory.remove(their_best)
            return True
        else:
            return False



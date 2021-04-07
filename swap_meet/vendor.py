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

    def get_by_category(self, category):
        category_list = []
        for items in self.inventory:
            print(items.category)
            if items.category == category:
                category_list.append(items)
        return category_list

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            vendor.add(my_item)
            vendor.inventory.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False

    def swap_first_item(self, other_vendor):
        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
        else:
            return False

    def get_best_by_category(self, category):
        if len(self.inventory) == 0:
            return None
        
        for item in self.inventory:
            if item.category != category:
                continue
            if 'best_so_far' not in locals():
                best_so_far = item
            if item.condition <= best_so_far.condition:
                continue
            best_so_far = item
        if 'best_so_far' not in locals():
            return None
        return best_so_far

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if my_best != None and their_best != None:
            self.swap_items(other, my_best, their_best)
            return True
        else:
            return False
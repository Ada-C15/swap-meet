from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

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
        return False
    
    def get_by_category(self, category_name):
        items = []
        for item in self.inventory:
            if category_name == item.category:
                items.append(item)
        return items
    
    def swap_items(self, vendor_friend, my_item, their_item):  
        if my_item not in self.inventory or their_item not in vendor_friend.inventory:
            return False
        else:
            self.remove(my_item)
            vendor_friend.remove(their_item)
            vendor_friend.add(my_item)
            self.add(their_item)
            return True
    
    def swap_first_item(self, vendor_friend):
        if len(self.inventory) == 0 or len(vendor_friend.inventory) == 0:
            return False
        else:
            item_a = self.inventory[0]
            item_d = vendor_friend.inventory[0]
            result = self.swap_items(vendor_friend, item_a, item_d)
            return result

    def get_best_by_category(self, category_name):
        highest_condition = 0
        best_item = None

        for item in self.get_by_category(category_name):
            if item.condition > highest_condition:
                highest_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        result = self.swap_items(other, my_best_item, their_best_item)
        return result


        


        






        


        

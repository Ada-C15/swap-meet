from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        # too strict a condition? replace with 'else:\n self.inventory = inventory'?
        elif type(inventory) == list: 
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
        hold_relevant_items = []
        list_to_check = self.inventory
        
        for item in list_to_check:
            if item.category == category:
                hold_relevant_items.append(item)
        
        return hold_relevant_items

    def swap_items(self, Vendor, my_item, their_item):
        vendor_prime = self
        vendor_second = Vendor

        if my_item in vendor_prime.inventory and their_item in vendor_second.inventory:
            vendor_prime.add(their_item)
            vendor_prime.remove(my_item)
            vendor_second.add(my_item)
            vendor_second.remove(their_item)
            return True
        else: 
            return False

    def swap_first_item(self, Vendor):
        if len(self.inventory) == 0 or len(Vendor.inventory) == 0:
            return False
        else:
            my_first_val = self.inventory[0]
            their_first_val = Vendor.inventory[0]
            self.swap_items(Vendor, my_first_val, their_first_val)
            return True

    def get_best_by_category(self, category):
        contenders = []
        for item in self.inventory:
            if item.category == category:
                contenders.append(item)
        if len(contenders) == 0:
            return None

        def get_condition(item):
            return item.condition

        contenders.sort(key=get_condition, reverse=True)
        highest_rated_item = contenders.pop(0)
        return highest_rated_item 


    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item_to_give = self.get_best_by_category(their_priority)
        their_best_item_to_give = other.get_best_by_category(my_priority)

        if my_best_item_to_give and their_best_item_to_give:
            self.swap_items(other, my_best_item_to_give, their_best_item_to_give)
            return True
        else: 
            return False

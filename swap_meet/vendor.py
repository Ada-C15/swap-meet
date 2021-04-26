from swap_meet.item import Item 

class Vendor:

    def __init__(self, inventory = []):
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
        self.category = category
        category_list = []

        for item in self.inventory:

            if item.category == category:
                category_list.append(item)

        return category_list

    def swap_items(self, other_vendor, my_item, their_item):
        
        self.other_vendor = other_vendor
        self.my_item = my_item
        self.their_item = their_item

        if (my_item in self.inventory) and (their_item in other_vendor.inventory):

            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)

            return True
        
        return False

    def swap_first_item(self, other_vendor):

        self.other_vendor = other_vendor

        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0:
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]

            self.inventory[0] = their_first_item
            other_vendor.inventory[0] = my_first_item
            return True

        else:
            return False

    def get_best_by_category(self, category):
        
        category_list = []
        top_counter = 0

        for item in self.inventory:
            if category == item.category:
                category_list.append(item)
        
        if len(category_list) == 0:
            return None 
            
        for best in category_list:
            if best.condition > top_counter:
                top_counter = best.condition
                best_item = best 

        return best_item
 
    
    def swap_best_by_category(self, other, my_priority, their_priority):
    
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if my_best_item and their_best_item:
            self.swap_items(other, my_best_item, their_best_item)
            return True 
        else:
            return False





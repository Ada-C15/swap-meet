# WAVE ONE

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
        items_by_category = []
        for item in self.inventory:
            if item.category == category:
                items_by_category.append(item)
        return items_by_category 

    def swap_items(self, vendor_friend, my_item, their_item):
        if my_item not in vendor_friend.inventory and my_item in self.inventory and their_item in vendor_friend.inventory and their_item not in self.inventory:
            self.remove(my_item)
            vendor_friend.add(my_item)
            vendor_friend.remove(their_item)
            self.add(their_item)
            return True  
        else:
            return False 

    def swap_first_item(self, vendor_friend):
        if self.inventory and vendor_friend.inventory:
            my_item = self.inventory[0]
            their_item = vendor_friend.inventory[0]
            self.swap_items(vendor_friend, my_item, their_item)
            return True
        return False 
        
        
    def get_best_by_category(self, category = ""):
        like_category = self.get_by_category(category)
        if len(like_category) == 0:
            return None 
        best_condition = like_category[0]
        for item in like_category:
            if item.condition > best_condition.condition:
                best_condition = item 
        return best_condition 


    def swap_best_by_category(self, other, my_priority, their_priority):
        item_to_give = self.get_best_by_category(their_priority)
        item_to_get = other.get_best_by_category(my_priority)
        swapped = self.swap_items(other, item_to_give, item_to_get)
        return swapped 


        
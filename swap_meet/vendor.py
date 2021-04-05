

class Vendor:
    
    def __init__(self, inventory = None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []

    def add(self, new_item):
        
        self.inventory.append(new_item)
        return new_item 

#removes item_to_remove from self's inventory
    def remove(self, item_to_remove):
        for item in self.inventory:
            if item == item_to_remove:
                self.inventory.remove(item_to_remove)
                return item_to_remove 
        return False

    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
            if item.category == category:
                items_list.append(item)
        return items_list

    def swap_items(self, vendor_friend, my_item, their_item):
        if self.remove(my_item):
            if vendor_friend.remove(their_item):
                vendor_friend.add(my_item)
                self.add(their_item)
                return True
            else: 
                self.add(my_item)
        return False

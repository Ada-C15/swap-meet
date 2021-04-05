

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


    def swap_first_item(self, vendor_friend):
        if len(self.inventory) != 0 and len(vendor_friend.inventory) != 0:
            first_item = self.inventory.pop(0)
            friend_first_item = vendor_friend.inventory.pop(0)
            self.add(friend_first_item)
            vendor_friend.add(first_item)
            return True
        return False

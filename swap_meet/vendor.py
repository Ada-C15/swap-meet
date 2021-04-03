from swap_meet.item import Item

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
    
    def swap_items(self, friend_vendor, my_item, their_item):
        
        if my_item not in self.inventory or their_item not in friend_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            friend_vendor.remove(their_item)
            friend_vendor.add(my_item)
            self.add(their_item)
            return True





        


        

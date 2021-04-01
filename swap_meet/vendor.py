class Vendor:
    # wave 01
    def __init__(self, inventory=None):
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
            
        self.inventory.remove(item)
        return item

    # wave 02
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    #  wave 03
    def swap_items(self, friend, item_1, item_2):
        my_inventory = set(self.inventory)
        friend_inventory = set(friend.inventory)
        if item_1 in my_inventory and item_2 in friend_inventory:
            self.inventory.remove(item_1)
            friend.inventory.append(item_1)
            self.inventory.append(item_2)
            friend.inventory.remove(item_2)
            return True        
        return False
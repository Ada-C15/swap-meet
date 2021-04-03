class Vendor:
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
        else: 
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        
        return items

    def swap_items(self, vendor, my_item, their_item):
        my_inventory = self.inventory
        friend_inventory = vendor.inventory
        if my_item in my_inventory and their_item in friend_inventory:
            friend_inventory.append(my_item)
            my_inventory.remove(my_item)
            my_inventory.append(their_item)
            friend_inventory.remove(their_item)
            return True
        return False

    def swap_first_item(self, vendor):
        if len(self.inventory) >= 1 and len(vendor.inventory) >= 1:
            my_first_item = self.inventory[0]
            friend_first_item = vendor.inventory[0]

            vendor.inventory.insert(1, my_first_item)
            self.inventory.insert(1, friend_first_item)

            del self.inventory[0]
            del vendor.inventory[0]

            return True

        return False

            

    
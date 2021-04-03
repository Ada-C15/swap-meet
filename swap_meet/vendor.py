
class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else: 
            self.inventory = inventory 
        
    def adding_to_inventory(Vendor): #checks item in inventory & returns True or False 
        if item in inventory:
            self.inventory.add(item)
        else:
            self.inventory.remove(item)
        return False 
    
    def add(self, item): #append item in inventory 
        self.inventory.append(item)
        return item

    def remove(self, item): #remove item from inventory
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False 
            
        return item 

    def get_by_category(self, category):
        """
        gets items by category
        input: inventory from items
        output: list of category 

        """
        item_by_category = []
        for item in self.inventory:
            if item.category == category:
                item_by_category.append(item)
        return item_by_category


    def swap_items(self, friend_vendor, my_item, their_item):
        """
        check inventory items of each Vendor
        input: adds and removes items from each Vendor inventory 
        output: Return True or False 
        """
        if my_item in self.inventory and their_item in friend_vendor.inventory:
            self.add(their_item)
            self.remove(my_item)
            friend_vendor.add(my_item)
            friend_vendor.remove(their_item)
            return True 
        else:
            return False 

    def swap_first_item(self, friend):
        """
        checks 1st item in self.inventory & friend's inventory
        input: remove 1st items from self & friend
        output: adds 1st items to self & friend. Returns True or False 
        """
        if self.inventory and friend.inventory:
            own_item = self.inventory[0]
            friend_item = friend.inventory[0]

            self.remove(own_item)
            friend.add(own_item)
            friend.remove(friend_item)
            self.add(friend_item)
            return True 
        else:
            return False
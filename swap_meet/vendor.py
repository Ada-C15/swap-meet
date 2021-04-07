from swap_meet.item import Item
# You need to run the file from the root directory (swap-meet) using a relative path like so: $ python3 -m swap_meet.vendor 

class Vendor:
    # Vendor() has an attribute 'inventory' which is by default an empty list, and Vendor() takes an argument 'inventory'
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self, item):
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item

    # Vendor has an instance method get_by_category(category) with 1 parameter (category) 
    def get_by_category(self, category):
        
        items = []

        # for each item Vendor's inventory, compares the passed-in 'category' to the item's 'category' attribute
        for item in self.inventory:
            # if they match, the method returns a list of the items in the Vendor's inventory with the matching attribute
            if item.category == category:
                items.append(item)
            # if they don't match, nothing happens, which is fine, and items gets returned as is:
        return items 

    def swap_items(self, friend, my_item, their_item):
        
        # guard clause (method cannot find my_item or their_item in either inventory list and/or inventories are empty)  
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        # take my_item out of my inventory list and adds it to friend's inventory
        self.remove(my_item)
        friend.add(my_item)

        # takes their_item out of friend's inventory and adds it to my inventory
        friend.remove(their_item)
        self.add(their_item)

        return True

    def swap_first_item(self, friend):

        # guard clause
        if not self.inventory or not friend.inventory:
            return False

        # removes first item in `inventory` of `friend` and adds to `inventory` of recipient Vendor
        friend_first_item = friend.inventory[0]
        
        friend.remove(friend_first_item)
        self.add(friend_first_item)

        # removes first item in `inventory` of recipient Vendor and adds to `inventory` of `friend`
        self_first_item = self.inventory[0]
        self.remove(self_first_item)
        friend.add(self_first_item)

        return True

    def get_best_by_category(self, category):

        best_item_condition = 0
        best_item = 0
        
        # loopin' through stuff
        for item in self.inventory:
            # if the '`category` attribute of `item` matches the argument passed into `get_best_by_category()` AND if the item's condition rating > highest found so far in loop:
            if item.category == category and item.condition >= best_item_condition:
                # update the best_item variables to reflect the best-condition item found so far  
                best_item_condition = item.condition
                best_item = item
        
        # (?) wondering if there is a way to make this into a guard clause instead of having to put this after the loop:
        if best_item == 0:
            return None
    
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):

        if not self.inventory or not other.inventory:
            return False

        for my_item in self.inventory:
            if my_item.category == their_priority:
                other.add(my_item)
                self.remove(my_item)
        
        for other_item in other.inventory:
            if other_item.category == my_priority:
                self.add(other_item)
                other.remove(other_item)
        
        return True



        

        

        


        
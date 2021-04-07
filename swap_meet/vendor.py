
class Vendor:
    def __init__(self, inventory = None): 
        if inventory == None:
            self.inventory = []      # instances
        else:
            self.inventory = inventory
            
    # call other instances with self.
    def add(self, item):   # adds item to inventory and returns item
        self.inventory.append(item)
        return item
            
    def remove(self, item): # removes item from inventory and returns item
        if item not in (self.inventory):
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_category(self, category): # puts items in inventory list by category
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list



    def swap_items(self, friend, my_item, their_item): # swap my item and friend item
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False 

        #refactored 
        self.remove(my_item)
        friend.add(my_item)
        
        friend.remove(their_item)
        self.add(their_item)
        return True


        # # orginal version below
        # self.inventory.remove(my_item)
        # friend.inventory.append(my_item)
        # friend.inventory.remove(their_item)
        # self.inventory.append(their_item)
        # return True 



    def swap_first_item(self, friend):   # swap our first items
        # refactored
        if len(self.inventory) <= 0 or len(friend.inventory) <= 0:  # if inventory is empty return False
            return False 
        
        # refactored code 
        my_first_item = self.inventory[0]  # first item in inventory
        friend_first_item = friend.inventory[0] # friends first item in inventory

        self.swap_items(friend, my_first_item, friend_first_item)
        return True

        # # original code 
        # self.inventory.remove(self.inventory[0])
        # self.inventory.insert(0, friend.inventory[0])

        # friend.inventory.remove(friend.inventory[0]
        # friend.inventory.insert(0, self.inventory[0])
        # return True

        

    def get_best_by_category(self, category): # find my best item agaisnt their best item
        highest_condition = 0
        best_item = None
        
        for item in self.inventory:
            if item.condition > highest_condition and category == item.category: # passing in friends item to look for category
                highest_condition = item.condition
                best_item = item
        return best_item


    def swap_best_by_category(self, other, my_priority, their_priority): # Swap my best item with their best item
        
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if my_best_item == None or their_best_item == None:
            return False
        else: 
            self.swap_items(other, my_best_item, their_best_item)
            return True 
        



    


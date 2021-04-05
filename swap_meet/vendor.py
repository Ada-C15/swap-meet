class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else: 
            self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item 
        
        
    def remove(self, removed_item):
        for inventory_item in self.inventory:
            if inventory_item is removed_item:
                self.inventory.remove(removed_item)
                return removed_item
        return False

    def get_by_category(self, category = ""):
        items = []
        for inventory_item in self.inventory:
            if(inventory_item.category is category):
                items.append(inventory_item)
        return items
    
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory:
            return False
        if their_item not in friend.inventory:
            return False
        self.inventory.remove(my_item)
        friend.inventory.append(my_item)
        
        friend.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True
    
    def swap_first_item(self, friend):
        # had to put this first so that i coulf run through my code *(checking function first)
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False 
        # Takes the fist item using the key holds that data in my variable 
        self_item = self.inventory[0]
        friend_item = friend.inventory[0]
        #This adds the last key items that I took out of the above list.
        
        self.inventory[0] = friend_item
        friend.inventory[0] = self_item
        #Made sure to add True at the end so that it wont end my function 
        return True
    def get_best_by_category(self, catergory):
        for item in self.
        



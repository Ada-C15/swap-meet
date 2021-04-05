class Vendor:
    
    def __init__(self, inventory = None):
        
        #self.inventory = inventory
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    # method, adds item to self.inventory[]
    def add(self,item):
        if item not in self.inventory:
            self.inventory.append(item)
        return item 
    
    # returns and removes item if it is found in the inventory list
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    # .category is referencing category in Item class. This method returns list of items that match type_of_stuff category
    def get_by_category(self, type_of_stuff):
        categorlist = []
        for item in self.inventory:
            if item.category == type_of_stuff:
                categorlist.append(item)
        return categorlist

   
    def swap_items(self, swapping_vendor, my_item, their_item):
        
        if my_item not in self.inventory or their_item not in swapping_vendor.inventory:
            return False
        
        else:
            self.remove(my_item)
            self.add(their_item)
            swapping_vendor.remove(their_item)
            swapping_vendor.add(my_item)        
        return True
       
        
    def swap_first_item(self,vendor_friend):
        # method looks at self and vendor_friend first item in their inventories 
        # removing first item in self.inventory and replacing it with vendor_friends first item
        # adding item to vendor_friend.inventory 
        if len(self.inventory) == 0 or len(vendor_friend.inventory) == 0:
            return False
        
        else:
            self_first = self.inventory[0]
            friend_first = vendor_friend.inventory[0]
        
            self.remove(self_first)
            vendor_friend.inventory.remove(friend_first)
            self.add(friend_first)
            vendor_friend.add(self_first)
        return True 
    
    def get_best_by_category(self, category):
        
        list_of_items  = self.get_by_category(category)
        
        for item in list_of_items:
            if list_of_items == []:
                return None 
        highest_num = 0
        for item in list_of_items:
            if item.condition > highest_num:
                highest_num = item.condition
        for item in list_of_items:
            if highest_num == item.condition:
                return item 
    
    def swap_best_by_category(self, other, my_priority,their_priority):
 
        my_list = self.get_by_category(their_priority)
        other_vendor_list = other.get_by_category(my_priority)
        
        if my_list == [] or other_vendor_list == []:
            return False
        
        other_vendor_best = other.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)

        self.swap_items(other,my_best,other_vendor_best)
        other.swap_items(self,other_vendor_best,my_best)  
        return True   # i want to use swap_items(self, swapping_vendor, my_item, their_item):





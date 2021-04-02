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
        
        if their_item not in self.inventory or my_item not in swapping_vendor.inventory:
            return False
        
        else:
            self.inventory.remove(my_item)
            self.inventory.add(their_item)
            swapping_vendor.remove(their_item)
            swapping_vendor.add(my_item)        
            return True
       
        
    def swap_first_item(self,vendor_friend):
        # method looks at self and vendor_friend first item in their inventories 
        # removing first item in self.inventory and replacing it with vendor_friends first item
        # adding item to vendor_friend.inventory 
       pass
       
        # if self.inventory == [] or vendor_friend.inventory == []:
        #     return False
        
        #  first_element = self.inventory.remove(self.inventory[0]):


        # removing first item from self.inventory
        # add this item to vendor_friend.inventory 
        # removes first item from vendor_friend.inventory 
        # add this item to self.inventory
        # return True
    

    


class Vendor:    
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory 
    
    def add(self, item):
        """
        Adds item to the inventory 
        Args:
            item (Item): inventory list
        Returns:
            item: added item
        """        
        (self.inventory).append(item) 
        return item

    def remove(self, item): 
        """
        Removes the matching item from the inventory
        Args:
            item (Item): inventory list
        Returns:
            item: removed item
        """        
        item_index = None
        for index in range(len(self.inventory)):
            if item == self.inventory[index]:
                return self.inventory.pop(index)
        return False

    def get_by_category(self, category):
        """
        Returns a list of Items in the inventory with that category  
        Args:
            category (string): attribute of class Item
        Returns:
            list: list of Items in the inventory with the category
        """        
        return [item for item in self.inventory if item.category == category] 
    
    def swap_items(self, friend_vendor, my_item, their_item):
        """
        It removes my_item from this Vendor's inventory, and adds it 
        to the friend_vendor inventory. It removes the their_item
        from the friend_vendor inventory, and adds it to this 
        Vendor's inventory
        Args:
            friend_vendor (Vendor): an instance of another Vendor
            my_item (Item): an instance of this Vendor's Item 
            their_item (Item): an instance of friend_vendor (Vendor) 
            Item 
        Returns:
            Boolean: True if swap is successful, False otherwise.
        """        
        friend_list = friend_vendor.inventory  
        my_list = self.inventory  
        if their_item in friend_list and my_item in my_list \
            and their_item != None and my_item != None and my_list != []\
            and friend_list !=[]:
            their_removed = friend_vendor.remove(their_item)
            my_removed  = self.remove(my_item) 
            friend_list.append(my_removed)
            my_list.append(their_removed)
            return True
        else:
            return False

    def swap_first_item(self, friend_vendor):
        """
        Swaps first item from its inventory, with friend's first item
        each inventory
        Args:
            friend_vendor (Vendor): Instance of another Vendor
        Returns:
            Boolean: True if swap is successful, False otherwise.
        """        
        friend_list = friend_vendor.inventory  
        my_list = self.inventory 
        if  my_list != [] and friend_list !=[]:
            their_removed = friend_vendor.remove(friend_list[0])
            my_removed  = self.remove(self.inventory[0]) 
            friend_list.append(my_removed)
            my_list.append(their_removed)
            return True
        else:
            return False   

    def get_best_by_category(self, category):
        """
        Get the item with the best condition in a certain category
        Args:
            category (string): [description]
        Returns:
            Item: returns a single item even if there are duplicates 
            (two or more of the same item with the same condition)
        """        
        items_by_category = self.get_by_category(category)
        if len(items_by_category) == 0:
            return None
        best_item = items_by_category[0]
        for item in items_by_category:
            if best_item.condition < item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, \
        their_priority):
        """
        Swaps the best item of certain categories with another Vendor
        Args:
            other (Vendor): instance of Vendor to trade with
            my_priority (string): category that this Vendor wants to receive
            their_priority (string): category that other Vendor wants to
            receive
        Returns:
            Boolean: True if swap is successful, False otherwise.
        """        
        my_item = self.get_best_by_category(their_priority)  
        their_item = other.get_best_by_category(my_priority) 
        swap = self.swap_items(other, my_item, their_item)
        return swap

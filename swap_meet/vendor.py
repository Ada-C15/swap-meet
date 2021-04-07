class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
 
    def add(self, item):
        """
        function: adds Item to inventory 
        input: Item to add
        output: Item (list)
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        """
        function: removes Item from inventory 
        input: Item to remove
        output: Item list if True, or False
        """

        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        """
        function: groups the items by category passed in
        """

        by_category_list = []
        for item in self.inventory:
            if item.category == category:
                by_category_list.append(item)
        return by_category_list
        
   
    def swap_items(self, vendor,my_item,vendor_item ): 
        """
        function: checks Items are in inventory 
        input: Self, Vendor and Items to swap
        output: Booleon (True for success)
        """
     
        if my_item in self.inventory and vendor_item in vendor.inventory:
            self.add(vendor_item)
            self.remove(my_item)
            vendor.remove(vendor_item)
            vendor.add(my_item)
            return True
        return False
    
   
    def swap_first_item(self,vendor):
        """
        function: swaps and removes item
        input: vendor
        output: True if successful, or False if empty list for vendor encountered
        """
        if self.inventory == [] or vendor.inventory == []:
            return False

        self_first_item = self.inventory[0]
        vendor_first_item = vendor.inventory[0]
        self.remove(self_first_item)
        self.add(vendor_first_item)
        vendor.remove(vendor_first_item)
        vendor.add(self_first_item)
        return True

    
    def get_best_by_category(self,category):
        """
        function: Gets all the items by category
        input: category
        output: True if successful, or False if empty list for vendor encountered
        """
        if self.get_by_category == None:
            return None

        best_item = None
        for item in self.get_by_category(category):
            if best_item == None or item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self,other,my_priority,their_priority):
        # my_priority is category that the Vendor wants to receive
        # their_priority represents the category the other Vendor wants
        """
        function: Best item in inventory that matches category is swapped with the best item in `other`'s inventory that matches `my_priority`
        input: `their_priority`, my priority, other (the other vendor)
        output: Boolean.  

        False -- If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False.  - If `other` has no item that matches `my_priority` category, swapping does not happen, and it returns `False`
        """
        
        if other.get_by_category(my_priority) == None or self.get_by_category(their_priority)== None:
            return False

        my_trade_to_other = self.get_best_by_category(their_priority)
        their_trade_to_me = other.get_best_by_category(my_priority)

        result = self.swap_items(other,my_trade_to_other,their_trade_to_me)
        return result
        
        

        


       



           


       
       
       


        

        

        
        

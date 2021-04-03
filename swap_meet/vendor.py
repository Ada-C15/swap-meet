# from .item import Item # Do I need this

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
        function: checks Items are in inventory 
        input: Self, Vendor and Items to swap
        output: Booleon (True for success)
        """
        by_category_list = []
        # print("Category:", category)
        for item in self.inventory:
            #print("item>>", item)
            if item.category == category:
                # print("I am category clothing")
                by_category_list.append(item)
        return by_category_list
        
   #wave 3  
    def swap_items(self, vendor,my_item,vendor_item ): 
        """
        function: checks Items are in inventory 
        input: Self, Vendor and Items to swap
        output: Booleon (True for success)
        """
        #self is fatimah
        # self.inventory #Fatimah
        # print(vendor.inventory)
        if vendor.inventory == []:
            return False
        if my_item in self.inventory and vendor_item in vendor.inventory:
            self.add(vendor_item)
            self.remove(my_item)
            vendor.remove(vendor_item)
            vendor.add(my_item)
            return True
        return False
    
    #wave 4

    def swap_first_item():
        pass
        

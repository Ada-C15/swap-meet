from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        ''' 
        Input: an item 
        Output: the Input item that was added to the inventory
        '''
        result = self.inventory.append(item)
        return item

    def remove(self, item):
        ''' 
        Input: an item 
        Output: Either the the Input item that was 
        removed from the inventory or False
        '''
        if item in self.inventory:
            result = self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        ''' 
        Input: a category used to help get an item by category
        Output: a list of items within the same category
        '''
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, other_vendor, vendor_item, other_vendor_item):
        '''
        Input: the vendor to swap with, 
        the orginal vendor's item and the other vendor's item

        Output: Returns False if the items are not in either vendors inventory. 
        If if both items are avialble the code returns True and switches 
        other_vendor_item with vendor_item and vis versa. 
        Also removes the items switched from each inventory.
        '''
        if (vendor_item not in self.inventory or 
        other_vendor_item not in other_vendor.inventory):
            return False
        else:
            for item in other_vendor.inventory:
                if item == other_vendor_item:
                    self.inventory.append(item)
                    other_vendor.inventory.remove(item)
            for item in self.inventory:
                if item == vendor_item:
                    other_vendor.inventory.append(item)
                    self.inventory.remove(item)
            return True

    def swap_first_item(self, other_vendor):
        '''
        Input: the vendor to swap with.
        Output: Returns False if either the vendor or other_vendor 
        inventory is an empty list. If neither are empty lists the code
        implements the swap.item method to swap the first item of each 
        inventory with the other and removes the items from their orginal lists.
        '''
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            self.swap_items(other_vendor,self.inventory[0],other_vendor.inventory[0])
            return True

    def get_best_by_category(self, category):
        '''
        Input: the category to filer by.
        Output: Returns the item with the largest condition 
        and that matches the same type of category as the input.
        '''
        largest_num = 0
        largest_item = None
        for item in self.inventory:
            if category == item.category:
                if item.condition > largest_num:
                    largest_num = item.condition
                    largest_item = item
        return largest_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Input: the vendor to swap with, 
        the orginal vendor's item and the other vendor's item

        Output: Returns False if either vendor or other's inventory are empty lists.
        If both inventories are not empty lists the code returns True and uses the method
        get_best_category and the approprate argument to find the best condition. 
        The code and uses the method swap_item to swap my_priority and their_priority.
        '''
        if self.inventory == [] or other.inventory == []:
            return False
        else:
            vendor_item = other.get_best_by_category(my_priority)
            other_item = self.get_best_by_category(their_priority)
            self.swap_items(other, other_item, vendor_item)

            return True
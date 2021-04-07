from swap_meet.item import Item

# ---- Wave 1 ----- #
class Vendor: 
    '''
    Represents a Vendor 
    Attributes: 
        inventory (list of items)
    '''

    def __init__(self, inventory=None):
        '''
        Initializes attributes of Vendor
        Parameters: 
            inventory which is optional and empty [] by default, can take in a list of items
        '''
        if inventory == None: 
            self.inventory = []
        else: 
            self.inventory = inventory 

    def add(self, item): 
        '''
        Adds one item to the vendor's inventory
        Parameters: 
            one item object of class Item 
        Returns: 
            one item object of class Item 
        '''
        self.inventory.append(item)
        return item
        
    def remove(self, item): 
        '''
        Removes one item that exists in the vendor's inventory and returns the item if found
        Parameters: 
            item
        Returns: 
            item or False
        '''
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else: 
            return False

# ---- Wave 2 ----- #
    def get_by_category(self, category): 
        '''
        Creates a list of items in a given category
        Parameters: 
            category (str)
        Returns: 
            list of items
        '''
        items_list = []
        for item in self.inventory: 
            if category == item.category: 
                items_list.append(item)
        return items_list 

# ---- Wave 3 ----- #
    def swap_items(self, friend, my_item, their_item):
        '''
        Swaps items of a given category between 2 vendors
        Parameters: 
            friend (Vendor), my_item (Item), their_item (Item)
        Returns: 
            True if exchange occured or False if exchange didn't occur
        '''
        swapped = False
        if my_item in self.inventory and their_item in friend.inventory:
            self.inventory.remove(my_item)
            friend.inventory.append(my_item)
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            swapped = True
        return swapped

# ---- Wave 4 ----- #
    def swap_first_item(self, friend): 
        '''
        Swaps first items in inventories of 2 vendors. 
        Parameters: 
            friend (Vendor)
        Returns: 
            True if exchange occured or False if exchange didn't occur
        '''
        if not self.inventory or not friend.inventory: 
            return False 
        return self.swap_items(friend, self.inventory[0], friend.inventory[0])

# ---- Wave 6 ----- #
    def get_best_by_category(self, category): 
        '''
        Gets items in given category and finds the item in the best condition. 
        Returns None if no item in given category was found.
        Parameters: 
            category (str)
        Returns: 
            best_item (Item) or None
        '''
        category_items = self.get_by_category(category)
        items_conditions = []
        best_item = None
        for item in category_items: 
            items_conditions.append(item.condition)
            best_condition = max(items_conditions)
            if best_condition == item.condition:  
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority): 
        '''
        Swaps vendor's best items by condition and in their preferred category.
        Parameters: 
            other (Vendor), my_priority (str), their_priority (str)
        Returns: 
            True if exchange occured or False if exchange didn't occur
        '''
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        return self.swap_items(other, my_best, their_best)

# ---- Optional Wave 7 ----- #
    def get_newest_by_category(self, category): 
        '''
        Gets items in given category and finds the newest item. 
        Returns None if no item in given category was found.
        Parameters: 
            category (str)
        Returns: 
            best_item (Item) or None
        '''
        category_items = self.get_by_category(category)
        items_ages = []
        newest_item = None 
        for item in category_items: 
            items_ages.append(item.age)
            newest_age = max(items_ages)
            if newest_age == item.age: 
                newest_item = item 
        return newest_item 
    
    def swap_newest_by_category(self, other, my_priority, their_priority): 
        '''
        Swaps vendor's newest items in their preferred category.
        Parameters: 
            other (Vendor), my_priority (str), their_priority (str)
        Returns: 
            True if exchange occured or False if exchange didn't occur
        '''
        my_newest = self.get_newest_by_category(their_priority)
        their_newest = other.get_newest_by_category(my_priority)
        return self.swap_items(other, my_newest, their_newest)

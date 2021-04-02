from .item import Item

class Vendor(Item):
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    '''
    This function takes two argument: a string, representing a category
    and an inventory that is optional. 
    Returns a list of Items in the inventory with that category
    Function created for wave 2
    '''
    def get_by_category(self, category):
        category_inventory = []
        for item in self.inventory:
            if item.category == category:
                category_inventory.append(item)
        return category_inventory
    

    '''
    This function takes 3 arguments: another friend Vendor, instance of an Item 
    (my_item) and another instance of an Item (their_item).
    It swaps items and return True in case items were in inventories, otherwise
    return False.
    Function created for wave 3
    '''
    def swap_items(self,vendor_friend, my_item, their_item):
        if my_item in self.inventory and \
            their_item in vendor_friend.inventory:
            self.inventory.remove(my_item)
            vendor_friend.inventory.append(my_item)
            vendor_friend.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False

    '''
    This function takes one argument: an instance of another Vendor
    representing a friend. Swap first element in both inventories
    (instance's inventory and friend's inventory)
    Return False if any inventory is empty
    Function created for wave 4
    '''
    def swap_first_item(self, vendor_friend):
        if not vendor_friend.inventory or not self.inventory:
            return False
        my_item = self.inventory[0]
        their_item = vendor_friend.inventory[0]
        return self.swap_items(vendor_friend, my_item, their_item)
    

    '''
    This function takes one argument: a category (str).
    Will return the item with bet condition, and if there is no
    item matching the category, will return None 
    Function created for wave 6
    '''
    def get_best_by_category(self, category):
        best_item = None
        best_condition = 0
        category_items = self.get_by_category(category)
        if len(category_items) != 0:
            for item in category_items:
                if item.condition > best_condition:
                    best_item = item
                    best_condition = item.condition
        return best_item
    
    '''
    This function takes three parameters: other Vendor, my priority for category
    and their priority for category.
    Swap items with the best items for each category.
    Return True is swap was succesful or False if no item matched.
    Function created for wave 6
    ''' 
    def swap_best_by_category (self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        return self.swap_items(other, my_best_item, their_best_item)
    

    '''
    This function takes one argument: a category (str).
    Will return the newest item and if there is no item matching 
    the category, will return None.
    Function created for Optional Enhancements
    '''
    def get_best_by_edge(self, category):
        newest_item = None
        edge = 1000
        category_items = self.get_by_category(category)
        if len(category_items) != 0:
            for item in category_items:
                if item.edge < edge:
                    newest_item = item
                    edge = item.edge
        return newest_item
    
        '''
    This function takes three parameters: other Vendor, my priority 
    for category and their priority for category.
    Swap items with the best items for each category.
    Return True is swap was succesful or False if no item matched.
    Function created for Optional Enhancements
    ''' 
    def swap_by_newest (self, other, my_priority, their_priority):
        my_newest = self.get_best_by_edge(their_priority)
        their_newest = other.get_best_by_edge(my_priority)
        return self.swap_items(other, my_best_item, their_best_item)







from swap_meet.item import Item


class Vendor():
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        ''' 
        Adds an item to inventory
        Parameters:
            item (str): the item to be added
        Returns:
            item (str): the item added
        '''
        self.inventory.append(item)
        return item

    def remove(self, item):
        ''' 
        Removes an item from inventory
        Parameters:
            item (str): the item to be removed
        Returns:
            item (str): the item removed
            False: if the item is not in inventory list
        '''
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category_string):
        '''
        Creates a list of items by category entered
        Parameters:
            category_string (str): represents a category
        Returns:
            items_based_on_category (list): inventory with that category
        '''
        items_based_on_category = []
        for items in self.inventory:
            if items.category == category_string:
                items_based_on_category.append(items)
        return items_based_on_category

    def swap_items(self, friends_vendor, my_item, their_item):
        '''
        Exchanges items between two vendor inventories
        Parameters:
            friends_vendor: instance of a different Vendor
            my_item: instance of an Item that this Vendor is giving 
            their_item: instance of an Item that friends_vendor is giving
        Returns:
            True:
            False: if my_item or their_item not in inventory
        '''
        if my_item in self.inventory and their_item in friends_vendor.inventory:
                self.add(their_item)
                self.remove(my_item)
                friends_vendor.add(my_item)
                friends_vendor.remove(their_item)
                return True
        return False
        
    def swap_first_item(self,friends_vendor):
        '''
        Exchanges the first item between two inventories
        Parameters: 
            friends_vendor: instance of a different vendor
        Returns:
            True:
            False: if either inventory is empty
        '''
        if len(self.inventory) == 0 or len(friends_vendor.inventory) == 0:
            return False 
        else:
            self.swap_items(friends_vendor, self.inventory[0],friends_vendor.inventory[0])
            return True

    def get_best_by_category(self, category):
        '''
        Gets the highest condition within the matching category
        Parameters:
            category (str): represents a category
        Returns:
            best_item (str): item with highest condition within category
            None: if their are no items within category
        '''
        list_by_category = self.get_by_category(category)
        if len(list_by_category) == 0:
            return None
        elif len(list_by_category) > 0:
            best_item = list_by_category[0]
            for items in list_by_category:
                if items.condition > best_item.condition:
                    best_item = items
            return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Exchanges the best item of a category with a different vendor
        Parameters:
            other: an instance of a different Vendor
            my_priority (str): category the vendor wants to recieve
            their_priorty (str): category the other vendor wants to recieve
        Return:
            True: if swapping occured
            False: if swapping does not happen
        '''
        my_category = other.get_best_by_category(my_priority)
        their_category = self.get_best_by_category(their_priority)
        return self.swap_items(other, their_category, my_category)
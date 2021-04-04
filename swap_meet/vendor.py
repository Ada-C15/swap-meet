class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        """
        Adds item to inventory.
        """
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        """
        Removes item from inventory. If the input item is not found in the inventory, returns False.
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        """
        Retuns a list of inventory items that are of the specified (input) category.
        """
        result = []
        for item in self.inventory:
            if item.category == category:
                result.append(item)
        return result

    def swap_items(self, other_vendor, my_item, other_item):
        """
        Input: the other Vendor object, and the items to swap. Returns false if either of these
        items-to-be-swapped are not valid. Returns true and swaps the items if they are valid.
        """
        if my_item not in self.inventory or other_item not in other_vendor.inventory:
            return False
        else:
            other_vendor.inventory.append(my_item)
            self.inventory.remove(my_item)
            self.inventory.append(other_item)
            other_vendor.inventory.remove(other_item)
            return True
    
    def swap_first_item(self, other):
        """
        Swaps the first item in this Vendor's inventory with the first item in the other
        vendor's inventory. Returns false if either inventory is empty.
        """
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False

        return self.swap_items(other, self.inventory[0], other.inventory[0])

    def get_best_by_category(self, category):
        """
        Input: a category. Looks for the items in the inventory that are of that category, and 
        returns the item with the highest condition rating. If there are no items of the specified
        category, returns None.
        """
        best_item = None
        best_item_condition = 0

        for item in self.inventory:
            if item.category == category:
                if item.condition > best_item_condition:
                    best_item = item
                    best_item_condition = item.condition

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Input: the other Vendor object, the category of item this Vendor object wants, and the category
        of item that the other Vendor object wants. Looks for the highest rated condition item under each
        specified category, and swaps those items. Returns False if either inventory is empty, or if no
        appropriate item is found in either inventory.
        """
        my_best_item_other_wants = self.get_best_by_category(their_priority)
        their_best_item_I_want = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_best_item_other_wants, their_best_item_I_want)

    def get_newest(self):
        """
        Returns the newest item (the item with the lowest age attribute) in the inventory.
        """
        newest_item = None
        newest_item_age = 999999999999999999999999999999999999

        for item in self.inventory:
            if item.age < newest_item_age:
                newest_item = item
                newest_item_age = item.age
        
        return newest_item

    def swap_by_newest(self, other):
        """
        Input: the other Vendor object. Looks for newest item in this Vendor object's inventory, and the newest
        item in the other Vendor object's inventory. Swaps those items. Returns False if either inventory
        is empty.
        """
        my_newest_item = self.get_newest()
        their_newest_item = other.get_newest()

        return self.swap_items(other, my_newest_item, their_newest_item)

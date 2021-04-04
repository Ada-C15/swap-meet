class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    """
    This method adds the provided argument to that object's inventory,
    and returns the argument. 
    """
    def add(self,item):
        self.inventory.append(item)
        return item

    """
    This method removes the provided argument, if it is already
    in the inventory, from that object's inventory and returns the argument.
    Otherwise, this method returns False.
    """
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    """
    This function iterates through all the items in the specified
    object's inventory and appends items whose category
    matches the provided category argument and returns the
    newly modified list.
    """
    def get_by_category(self,category):
        category_specific_list = []
        for item in self.inventory:
            if item.category == category:
                category_specific_list.append(item)
        return category_specific_list

    """
    This function swaps selected items (from the current object's inventory
    and anther instance of Vendor's inventory), but only if the
    items are actually in their respective inventories. 
    If an item is missing, the method returns False.
    """
    def swap_items(self, Vendor, my_item, their_item):
        if my_item in self.inventory and their_item in Vendor.inventory:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            Vendor.inventory.remove(their_item)
            Vendor.inventory.append(my_item)
            return True
        else:
            return False
    
    """
    This method swaps the first items from the current object's
    inventory and another instance of Vendor's inventory.
    If either inventory is empty, the method returns False.
    """
    def swap_first_item(self, Vendor):
        if Vendor.inventory == [] or self.inventory == []:
            return False
        else:
            self.inventory.append(Vendor.inventory[0])
            Vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0]) 
            Vendor.inventory.remove(Vendor.inventory[0])
            return True
    
    """
    This method returns the item in the current
    object's inventory (from the provided
    category) with the best condition rating. 
    """
    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        initial_condition = 0.0
        best_item = None
        for item in category_items:
            if item.condition > initial_condition:
                initial_condition = item.condition
                best_item = item
        return best_item

    """
    This method swaps the best item from each user's
    preferred category to the other object's inventory.
    If either inventory is empty, the function returns False,
    and if no items have a matching category (as the one
    provided in the argurments) None is returned. 
    """
    def swap_best_by_category(self, other, my_priority, their_priority):
        their_best_item = other.get_best_by_category(my_priority)
        my_best_item = self.get_best_by_category(their_priority)

        if self.inventory == [] or other.inventory == []:
            return False
        else:
            return self.swap_items(other, my_best_item, their_best_item)


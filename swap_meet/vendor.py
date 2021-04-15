class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        # self.inventory = inventory or []

    def __str__(self):
        return self.inventory

    def add(self, item):
        """
        adds the item to the inventory
        returns the item that was added
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        """
        removes the matching item from the inventory
        returns the item that was removed
        If there is no matching item in the inventory, the method should return False
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        """
        takes one argument: a string, representing a category
        returns a list of Items in the inventory with that category
        """
        same_category_items = []
        for item in self.inventory:
            if item.category == category:
                same_category_items.append(item)
        return same_category_items

    def swap_items(self, friend_vendor, my_item, friend_item):
        """
        takes 3 arguments
        imitates swap process
        """
        if (my_item in self.inventory) and (
                friend_item in friend_vendor.inventory):
            friend_vendor.add(self.remove(my_item))
            self.add(friend_vendor.remove(friend_item))
            return True
        return False

    def swap_first_item(self, friend_vendor):
        """
        takes one argument friend_vendor
        imitates swapping the first items in the friends inventory
        """
        if self.inventory and friend_vendor.inventory:
            return(self.swap_items(
                friend_vendor,
                self.inventory[0],
                friend_vendor.inventory[0]))
        return False

    def get_best_by_category(self, category):
        """
        gets the item with the best condition in a certain category
        """
        category_items_list = self.get_by_category(category)
        if len(category_items_list) > 0:
            item_with_best_condition = None
            for item in category_items_list:
                if (item_with_best_condition is None) or (
                        item.condition > item_with_best_condition.condition):
                    item_with_best_condition = item
            return item_with_best_condition
        return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        swaps the best item of certain categories with another Vendor
        """
        vendor_item_to_swap = self.get_best_by_category(their_priority)
        their_item_to_swap = other.get_best_by_category(my_priority)
        return self.swap_items(other, vendor_item_to_swap, their_item_to_swap)

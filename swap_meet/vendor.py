class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

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
        else:
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
        if self.inventory != [] and friend_vendor.inventory != []:
            self.swap_items(
                friend_vendor,
                self.inventory[0],
                friend_vendor.inventory[0])
            return True
        return False

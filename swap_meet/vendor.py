from .item import Item


class Vendor:
    """
    A class to represent a vendor

    Attributes
    inventory: list of items (default is [])
    """

    def __init__(self, inventory=None):
        """
        PARAMETERS: list of items, optional (default is [])
        """
        self.inventory = inventory
        if inventory is None:
            self.inventory = []

    def add(self, item):
        """
        Adds an item to the Vendor's inventory
        returns that same item
        PARAMETERS: Item
        OUTPUT: Item
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        """
        Removes and returns the item from the Vendor's inventory
        if the item was present.
        Otherwise returns False
        PARAMETERS: item
        OUTPUT: item or False
        """
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        """
        Return list of items in vendor's inventory that have a given category
        PARAMETERS: category str
        OUTPUT: item list
        """
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other, own_item, other_item):
        """
        Makes an item exchange between vendors
        PARAMETERS: other Vendor, own_item Item, other_item Item
        OUTPUT: bool (represents if the swap was successful)
        """
        if own_item not in self.inventory or other_item not in other.inventory:
            return False

        other.add(self.remove(own_item))
        self.add(other.remove(other_item))
        return True

    def swap_first_item(self, other):
        """
        Makes an exchange with the first item in two Vendors inventories
        PARAMETERS: other Vendor
        OUTPUT: bool (represents if the swap was successful)
        """
        if not self.inventory or not other.inventory:
            return False

        return self.swap_items(other, self.inventory[0], other.inventory[0])

    def get_best_by_category(self, category):
        """
        Gets item from vendor's inventory that matches a certain category and is
        in best condition. If no item is found returns None.
        PARAMETERS: category str
        OUTPUT: Item or None
        """
        if not self.get_by_category(category):
            return None

        return max(self.get_by_category(category), key=lambda x: x.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Swaps vendors items according to their category of preference and
        best condition available
        PARAMETERS: other Vendor, my_priority category str, their_priority category str
        OUTPUT: bool (represents if the swap was successful)
        """
        they_have = other.get_best_by_category(my_priority)
        i_have = self.get_best_by_category(their_priority)

        if not i_have or not they_have:
            return False

        return self.swap_items(other, i_have, they_have)

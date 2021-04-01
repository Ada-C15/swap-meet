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
        if inventory is None:
            self.inventory = []
        self.inventory = inventory

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

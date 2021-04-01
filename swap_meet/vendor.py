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
        """
        return [item for item in self.inventory if item.category == category]

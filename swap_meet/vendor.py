
class Vendor:
    """
    A class to represent a vendor

    Atributes
    inventory: list of items

    Methods
    add(item):
        adds an item to the inventory
    remove(item):
        remove item from the inventory
    """

    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        """
        Adds an item to the Vendor's inventory
        returns that same item
        INPUT: item
        OUTPUT: item
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        """
        Removes and returns the item from the Vendor's inventory
        if the item was present.
        Otherwise returns False
        INPUT: item
        OUTPUT: item or False
        """
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

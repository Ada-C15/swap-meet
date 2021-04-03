class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

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

    def get_by_category(category):
        if category in

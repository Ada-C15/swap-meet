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

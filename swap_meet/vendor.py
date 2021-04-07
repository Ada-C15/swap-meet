from .item import Item

class Vendor:
    """Creates instances of a vendor and their list of items. 

    If a Vendor object is instantiated without arguments, it's attributes will have default values.

    Attributes:
        inventory: An empty list by default. Instances can optionally pass in
            a list with the keyword argument `inventory`.
    """

    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        """Adds the `item` to the `inventory`.

        Args:
            item (str): The item to be added. 

        Returns:
            item (str): The item that was added.
        """

        self.inventory.append(item)
        return item

    def remove(self, item):
        """Removes the matching `item` from the `inventory`.

        Args:
            item (str): The item that will be removed.

        Returns:
            item (str): The item that was removed. If there is no matching item
                in the `inventory`, returns `False`.
        """

        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        """Iterates over the `inventory` to find the categories of the items in that list. 

        Args:
            category (str): Represents the `category` of the items.

        Returns:
            same_category_items: A list of `Item`s in the `inventory` with that
                `category`.
        """

        same_category_items = []
        for item in self.inventory:
            if item.category == category:
                same_category_items.append(item)
        return same_category_items

    def swap_items(self, friend, my_item, their_item):
        """Removes `my_item` from this `Vendor`'s `inventory` and adds it to the `friend`'s `inventory`.

        Args:
            friend (object): An instance of another `Vendor`, representing the
                friend that this `Vendor` instance is swapping with.

            my_item (str): Represents the item this `Vendor` instance plans to
                give.

            their_item (str): Represents the item the `friend` plans to give.

        Returns:
            bool: If this `Vendor`'s `inventory` doesn't contain `my_item` or
                the `friend`'s `inventory` doesn't contain `their_item`,
                returns `False`; otherwise, returns `True`.
        """

        if my_item in self.inventory and their_item in friend.inventory:
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            self.add(their_item)
            return True
        return False

    def swap_first_item(self, friend):
        """Swaps the first item in this `Vendor`'s `inventory` with the first item in the `friend`'s `inventory`.

        Args:
            friend (object): An instance of another `Vendor`, representing the
                friend that this `Vendor` instance is swapping with.

        Returns:
            bool: If either itself or the `friend` have an empty `inventory`,
                returns `False`. Otherwise, returns True.
        """

        if not self.inventory or not friend.inventory:
            return False
        else:
            my_item = self.inventory.pop(0)
            self.add(friend.inventory.pop(0))
            friend.add(my_item)
            return True

    def get_best_by_category(self, item_category):
        """Gets the item with the best `condition` in a certain `category`.

        Args:
            item_category (str): Represents the `category` of the items.

        Returns:
            best_item: A single item, even if there are duplicates (two or more
                of the same item with the same `condition`). If there are no
                items in the `inventory` that match the `category`, returns `None`.
        """

        best_cond = 0
        best_item = None

        for item in self.get_by_category(item_category):
            if item.condition > best_cond:
                best_item = item
                best_cond = item.condition
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """Swaps the best item of certain categories with another `Vendor`.

        Args:
            other (object): Represents another `Vendor` instance to trade with.

            my_priority (str): Represents a `category` that this `Vendor`
                instance wants to receive.

            their_priority (str): Represents a `category` that `other` wants
                to receive.

        Returns:
            bool: If any of both `Vendor` instances doesn't have an item that
                matches a desired `category`, returns `False`; otherwise,
                returns True.
        """

        mine = self.get_best_by_category(their_priority)
        theirs = other.get_best_by_category(my_priority)
        if not mine or not theirs:
            return False
        else:
            return self.swap_items(other, mine, theirs)

    def get_by_newest(self):
        """`swap_by_newest`s helper method.
        This is an instance method, so any instance can access to get the first newest `item` in their `inventory`.

        TODO:
            - Implement this method in a way that it also checks the categories
                or conditions of the items.
            - Have a special class for Vintage Items.

        Returns:
            newest_item: A single `item`, even if there are duplicates (two or 
                more of the same item with the same `condition`). 
                If there are no items in the `inventory` that match the `category`, returns `None`.
        """

        if self.inventory:
            newest_item = self.inventory[0]
            min_age = newest_item.age

            for item in self.inventory:
                if item.age < min_age:
                    newest_item = item
                    min_age = item.age
            return newest_item
        return None

    def swap_by_newest(self, friend):
        """Swaps the newest item in the inventory with another `Vendor`.

        Args:
            friend (object): An instance of another `Vendor`, representing the
                friend that this `Vendor` instance is swapping with.

        Returns:
            bool: If any of both `Vendor` instances doesn't have an item in
                their inventory, the swap does not occur; otherwise, returns True.
        """

        my_newest_item = self.get_by_newest()
        their_newest_item = friend.get_by_newest()

        if not my_newest_item or not their_newest_item:
            return False
        else:
            self.swap_items(friend, my_newest_item, their_newest_item)

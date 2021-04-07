from __future__ import annotations
# Necessary import for use of the Vendor type inside its own class

from .item import Item
from typing import List, Literal, Union, TypeVar, Generic

# BasicVendor class that uses str items or Items
# For use in test_wave_01.py

T = TypeVar('T', str, Item)


class BasicVendor(Generic[T]):
    """
    A class to represent a vendor

    Attributes
    inventory: list of items (default is [])
    """

    def __init__(self, inventory: List[T] = None):
        """
        PARAMETERS: list of items, optional (default is [])
        """
        if inventory is None:
            inventory = []

        self._inventory = inventory

    def add(self, item: T) -> T:
        """
        Adds an item to the Vendor's inventory
        returns that same item
        """
        self.inventory.append(item)
        return item

    def remove(self, item: T) -> Union[T, Literal[False]]:
        """
        Removes and returns the item from the Vendor's inventory
        if the item was present.
        Otherwise returns False
        """
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item

    @property
    def inventory(self):
        return self._inventory


class Vendor(BasicVendor[Item]):
    """
    A class that extends BasicVendor with methods only supported for Items
    """

    def get_by_category(self, category: str) -> List[Item]:
        """
        Return list of items in vendor's inventory that have a given category
        """
        return [item for item in self.inventory if item.category == category]

    def swap_items(
            self, other: Vendor, own_item: Item, other_item: Item) -> bool:
        """
        Makes an item exchange between vendors
        OUTPUT: represents if the swap was successful
        """
        if own_item not in self.inventory or other_item not in other.inventory:
            return False

        my_item = self.remove(own_item)
        their_item = other.remove(other_item)

        if my_item and their_item:
            other.add(my_item)
            self.add(their_item)
            return True

        return False

    def swap_first_item(self, other: Vendor) -> bool:
        """
        Makes an exchange with the first item in two Vendors inventories
        OUTPUT: represents if the swap was successful
        """
        if not self.inventory or not other.inventory:
            return False

        return self.swap_items(other, self.inventory[0], other.inventory[0])

    def get_best_by_category(self, category: str) -> Union[Item, None]:
        """
        Gets item from vendor's inventory that matches a certain category and is
        in best condition. If no item is found returns None.
        """
        if not self.get_by_category(category):
            return None

        return max(self.get_by_category(category), key=lambda x: x.condition)

    def swap_best_by_category(
            self, other: Vendor, my_priority: str, their_priority: str) -> bool:
        """
        Swaps vendors items according to their category of preference and
        best condition available
        OUTPUT: represents if the swap was successful
        """
        they_have = other.get_best_by_category(my_priority)
        i_have = self.get_best_by_category(their_priority)

        if not i_have or not they_have:
            return False

        return self.swap_items(other, i_have, they_have)

    def get_newest(self) -> Union[Item, None]:
        """
        Returns the item with the smallest non zero age.
        Otherwise it returns None
        """
        items = [item for item in self.inventory if item.age != 0.0]
        if not items:
            return None

        return min(items, key=lambda item: item.age)

    def swap_by_newest(self, other: Vendor) -> bool:
        """
        Swaps vendors items according to the items with the smallest non zero age
        OUTPUT: represents if the swap was successful
        """
        my_newest = self.get_newest()
        other_newest = other.get_newest()

        if not my_newest or not other_newest:
            return False

        return self.swap_items(other, my_newest, other_newest)

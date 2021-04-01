# Necessary import for use of the Item type inside its own class
from __future__ import annotations


class Item:
    """
    A class to represent an Item

    Attributes
    category: str (default is "")
    condition: float (default is 0)
    """

    def __init__(self, category: str = "", condition: float = 0):
        """
        PARAMETERS: category str (defaults to "")
                    condition float (defaults to 0)
        """
        self.category = category
        self.condition = condition

    def __str__(self) -> str:
        return "Hello World!"

    def __eq__(self, other: Item) -> bool:
        if self.category == other.category and self.condition == other.condition:
            return True
        return False

    def condition_description(self) -> str:
        """
        Returns a descriptive phrase according to the item's condition
        """
        if self.condition < 1.0:
            return "Maybe it could be upcycled??"
        elif self.condition < 2.5:
            return "It has seen better days, but maybe you could call it 'vintage'."
        elif self.condition < 3.5:
            return "It has a good amount of life left in it!"
        elif self.condition < 4.5:
            return "Used a couple times, wasn't appreciated. Looking for new love."
        elif self.condition < 4.9:
            return "Basically new. Like the latest emoji package (will you ever catch up with them? who knows??)!"
        else:
            return "Brand new"

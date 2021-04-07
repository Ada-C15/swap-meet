class Item:
    """Represents an item. Parent class for `Clothing`, `Decor`, and `Electronics` child classes. `Vendor` instances can have `Item` instances in their `inventory`.

    Attributes:
        condition (int): An optional attribute that defaults to 0 when not
            passed into an `Item` object instance. Used to reference an item's
            description based in values that range from 0 to 5, where 0
            describes an item in "Poor" condition, and 5 describes an item 
            that is "Like New".

        category (str): An empty string by default. Represents the category 
            of an item. Instances can optionally pass in a string with the
            keyword argument `category`.
    """

    def __init__(self, category=""):
        self.condition = 0
        self.category = category
        self.age = 0

    # Wave 5

    def condition_description(self):
        """Instance method that describes the condition of an item in words based on its `condition`, in a range from 0 to 5. 
        
        Child classes inherit this method as-is, but are able to override it if necessary. The one requirement is that the `condition_description` for all three classes above have the same behavior.

        Returns:
            [type]: [description]
        """

        descriptions = {
        5: "Like New",
        4: "Mint",
        3: "Very Good",
        2: "Good",
        1: "Fair",
        0: "Poor"
        }

        if self.condition not in descriptions:
            return None
        return descriptions[self.condition]

    def __str__(self):
        """Printable string representation of an Item instance."""        
        return "Hello World!"

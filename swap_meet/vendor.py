from .item import Item 

#Wave 1
# the attributes are the list of items/invetory and the class is vendor

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
        return

    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
        


        # - Instances of `Vendor` have an instance method named `get_by_category`
#   - It takes one argument: a string, representing a category
#   - This method returns a list of `Item`s in the inventory with that category


#wave 1 read.me
# - There is a module (file) named `vendor.py` inside of the `swap_meet` package (folder)
'''- Inside this module, there is a class named `Vendor`
- Each `Vendor` will have an attribute named `inventory`, which is an empty list by default
- When we create initialize an instance of `Vendor`, we can optionally pass in a list with the keyword argument `inventory`

The remaining tests in wave 1 imply:

- Every instance of `Vendor` has an instance method named `add`, which takes in one item
- This method adds the item to the `inventory`
- This method returns the item that was added

- Similarly, every instance of `Vendor` has an instance method named `remove`, which takes in one item
- This method removes the matching item from the `inventory`
- This method returns the item that was removed
- If there is no matching item in the `inventory`, the method should return `False`'''

#import item to pass wave two tests
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

#wave two: 
    def get_by_category(self, category):
        matched = []
        for item in self.inventory:
            if item.category == category:
                matched.append(item)
        return matched 
#wave 3
    def swap_items(self, them, my_item, their_item):
        if their_item not in them.inventory or my_item not in self.inventory:
            return False 
        else:
            self.inventory.remove(my_item)
            them.inventory.append(my_item)
            them.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
#wave 4 
    def swap_first_item(self, them):
        if len(self.inventory) == 0 or len(them.inventory) == 0:
            return False
        return self.swap_items(them, self.inventory[0], them.inventory[0])




    











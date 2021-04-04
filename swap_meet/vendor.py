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
        
    def swap_items(self, vendor,  my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:  

            self.remove(my_item)
            vendor.add(my_item) 
            vendor.remove(their_item)
            self.add(their_item)
            return True  
        return False


    def swap_first_item(self, vendor):
        if len(self.inventory) > 0 and len(vendor.inventory) > 0:
            return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        return False 

    def get_best_by_category(self, category):
        highest_condition_item = Item(category)
        item_exists = False
        for item in self.inventory:
            if item.category == category and item.condition > highest_condition_item.condition:
                highest_condition_item = item 
                item_exists = True
        if not item_exists: return None
        return highest_condition_item



            

### Wave 6

# The first three tests in wave 6 imply:

# - `Vendor`s have a method named `get_best_by_category`, which will get the item with the best condition in a certain category
#   - It takes one argument: a string that represents a category
#   - This method looks through the instance's `inventory` for the item with the highest `condition` and matching `category`
#     - It returns this item
#     - If there are no items in the `inventory` that match the category, it returns `None`
#     - It returns a single item even if there are duplicates (two or more of the same item with the same condition)

# The last three tests in wave 5 imply:

# - `Vendor`s have a method named `swap_best_by_category`, which will swap the best item of certain categories with another `Vendor`
#   - It takes in three arguments
#     - `other`, which represents another `Vendor` instance to trade with
#     - `my_priority`, which represents a category that the `Vendor` wants to receive
#     - `their_priority`, which represents a category that `other` wants to receive
#   - The best item in my inventory that matches `their_priority` category is swapped with the best item in `other`'s inventory that matches `my_priority`
#     - It returns `True`
#     - If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False`
#     - If `other` has no item that matches `my_priority` category, swapping does not happen, and it returns `False`
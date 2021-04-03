# Test 1 and 2
# Make a class Vendor with an attribute ( `inventory` empty list by default)  

# For TEST 1, 2 -  WAVE-01 PASSED!
class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory 
    
# For TEST 3 - WAVE-01  PASSED!
# - Method adds item to `inventory` -returns  item that was added
# takes in one item 
    def add(self, item):
        (self.inventory).append(item) 
        # list(self.inventory).append(item) ## ??? why can't I do  list(self.inventory).append(item)? and not declare inventory as inventory = []
        return item

#For TEST 4,5 WAVE-01  PASSED!
    # removes the matching item from the `inventory`
    # This method returns the item that was removed
    # If there is item not in `inventory` it returns `
    def remove(self, item):
        item_index = None
        for index in range(len(self.inventory)):
            if item == self.inventory[index]:
                return self.inventory.pop(index)
        return False
# https://www.geeksforgeeks.org/what-is-difference-between-del-remove-and-pop-on-python-lists/

# For TEST 7 & 8  WAVE 02
# method takes one argument: a string, representing a category
# Returns a list of `Item`s in the inventory with that categor       
    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]        

# FOR TEST WAVE 03 - PASSED?

# - When we stringify an instance of `Item` using `str()`, it returns `"Hello World!"`
#   - This implies `Item` overrides its stringify method


# The remaining 5 tests in wave 3 imply:
# - Instances of `Vendor` have an instance method named `swap_items`
#   - It takes 3 arguments: 
#       1. an instance of another `Vendor`, representing the friend that the vendor is swapping with
#       2. an instance of an `Item` (`my_item`), representing the item this `Vendor` instance plans to give
#       3. an instance of an `Item` (`their_item`), representing the item the friend `Vendor` plans to give
#   - It removes the `my_item` from this `Vendor`'s inventory, and adds it to the friend's inventory
#   - It removes the `their_item` from the other `Vendor`'s inventory, and adds it to this `Vendor`'s inventory
#   - It returns `True`
#   - If this `Vendor`'s inventory doesn't contain `my_item` or the friend's inventory doesn't contain `their_item`, the method returns `False`
# Test 1 and 2
# Make a class Vendor with an attribute ( `inventory` empty list by default)  

# For TEST 1 & 2 PASSED!
class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory 
    
# For TEST 3,  PASSED!
#`Vendor's` method  def `add`(self, item), 
# - This method adds the item to the `inventory`
# - This method returns the item that was added
    # takes in one item
    # inventory.append
        # return item  
    def add(self, item):
        (self.inventory).append(item) 
        # list(self.inventory).append(item) ## ??? why can't I do  list(self.inventory).append(item)? and not declare inventory as inventory = []
        return item

    def remove(self, item):
        item_index = None
        for index in range(len(self.inventory)):
            if item == self.inventory[index]:
                return self.inventory.pop(index)

        return False

# `Vendor` - method  `remove`(self, item)   
# https://www.geeksforgeeks.org/what-is-difference-between-del-remove-and-pop-on-python-lists/
        #  remove() Method:
        #The remove() method removes the first matching value from the list.
        # list_name.remove(value)
    #  removes the matching item from the `inventory`
    # if item in self.inventory:
        # self.inventory.remove(item)
        # return item
    # with pop()
    # probably have to do a for loop because I have to go over the list 
    # to find the index and that way return the value? Or can I do this 
    # with delete? 

# This method returns the item that was removed
# If there item not in `inventory`
    #  the method should return `False`
    # else return False

# For TEST 4 & 5
# - Instances of `Vendor` have an instance method named `get_by_category`
#   - It takes one argument: a string, representing a category
#   - This method returns a list of `Item`s in the inventory with that categor
        
    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category] 
        


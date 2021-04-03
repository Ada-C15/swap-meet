# Test 1 and 2

# For TEST 1, 2 -  WAVE-01 PASSED!
class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory 
    
# For TEST 3 - WAVE-01  PASSED!
    def add(self, item):
        (self.inventory).append(item) 
        # list(self.inventory).append(item) ## ??? why can't I do  list(self.inventory).append(item)? and not declare inventory as inventory = []
        return item

#For TEST 4,5 WAVE-01  PASSED!
    def remove(self, item): 
        item_index = None
        for index in range(len(self.inventory)):
            if item == self.inventory[index]:
                return self.inventory.pop(index)
        return False
# For TEST 7 & 8  WAVE 02      # Returns a list of `Item`s in the inventory with that category
    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category] 

# FOR TEST  (10, )WAVE 03 - 11, 12, 13, 14
    def swap_items(self, friend_vendor, my_item, their_item):
        friend_list = friend_vendor.inventory # ["planta", "gato", "hoja"]
        my_list = self.inventory # ["cel", "pluma", "piedra"]
        if their_item in friend_list and my_item in my_list \
            and their_item != None and my_item != None and my_list != []\
            and friend_list !=[]:
            their_removed = friend_vendor.remove(their_item)
            my_removed  = self.remove(my_item) 
            friend_list.append(my_removed)
            my_list.append(their_removed)
            return True
        else:
            return False

        

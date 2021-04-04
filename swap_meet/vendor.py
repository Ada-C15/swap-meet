############### TEST WAVE 1 (5 tests) PASSED ###############
############### TEST WAVE 2 (3 tests) PASSED ###############
############### TEST WAVE 4 (3 tests) PASSED ###############
# from item.swap_meet import Item - why is this not needed?

class Vendor:
    def __init__(self, inventory = None): #get_by_category,
    # you can't make an argument/parameter of a mutable data type
    # In python, if the inventory default is set to an empty list as the paramenter - then one instance update ...will change all the instances -
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
        # self.get_by_category = get_by_category() -- this is a Vendor method and does not need to be an attribute.

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if self.inventory == []:
            return None
        elif item not in self.inventory:
            return False
        else:
            for remove_item in self.inventory:
                if item == remove_item:
                    self.inventory.remove(remove_item)
                    return remove_item

### test 2.2 PASSED ###
### test 2.3 PASSED ###
    def get_by_category(self, category):
        items_by_category_list = []
        for item in self.inventory:
            if category == item.category: # syntax that refers to an item object by its category "str" 
                items_by_category_list.append(item)
        return items_by_category_list

# tests 2.2 and 2.3 are looking at ^ this Vendor class method
# get_by_category() is a Vendor class method. 
# ^^^It works with the many item-instances that belong to the Vendor-instance's inventory.
# tests 2.2
# ^^^returns a list of item-instances that belong to the category passed in.
# tests 2.3
#^^^returns an empty list if no item-instances belong to the category passed in.

### test 3.2 PASSED ###
### test 3.3 PASSED ###
### test 3.4 PASSED ###
### test 3.5 PASSED ###
### test 3.6 PASSED ###
    def swap_items(self, friendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in friendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            friendor.inventory.append(my_item)
            friendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True

    ### test 4.1 PASSED ###
    ### test 4.2 PASSED ###
    ### test 4.3 PASSED ###
    def swap_first_item(self, friendor):
        if self.inventory == [] or friendor.inventory == []:
            return False
        else:
            print("something else")
            friendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            self.inventory.append(friendor.inventory[0])
            friendor.inventory.remove(friendor.inventory[0])
            return True

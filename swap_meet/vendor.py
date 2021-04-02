from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self,item_name):
        self.inventory.append(item_name)
        return item_name

    def remove(self,item_name):
        if item_name in self.inventory:
            self.inventory.remove(item_name)
        else:
            return False
        return item_name
# Cd in terminal up 1 folder then run the specific 
# file w/ python3 -m swap_meet.vendor
    def get_by_category(self, category):
        category_list = []
        for items in self.inventory:
            print(items.category)
            if items.category == category:
            # if category == item.category:
                category_list.append(items)
        return category_list

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            # remove my item and give it to them
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            # remove their item and add to me
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False

    def swap_first_item(self, other_vendor):
        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0:
            # remove my first item and add to other vendor
            other_vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            # remove their first item and add to my invent. 
            self.inventory.append(other_vendor.inventory[0])
            other_vendor.inventory.remove(other_vendor.inventory[0])

            return True
        else:
            return False




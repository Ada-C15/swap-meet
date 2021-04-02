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
    
    def get_by_category(self, category):
        category_list = []
        for items in self.inventory:
            print(items.category)
            if items.category == category:
            # if category == item.category:
                category_list.append(items)
        return category_list

# Cd in terminal up 1 folder then run the specific 
# file w/ python3 -m swap_meet.vendor


from .item import Item


class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory or []
        
        # if inventory == None:
        #     self.inventory = []
        # else:
        #     self.inventory = inventory
        
        # self.inventory = inventory
        # if self.inventory is None:
        #     self.inventory = []
  
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, other_vendor, item_x, item_y):
        if item_x not in self.inventory or item_y not in other_vendor.inventory:
            return False
        item_being_swapped = self.remove(item_x)
        other_vendor.add(item_being_swapped)
        item_being_swapped = other_vendor.remove(item_y)
        self.add(item_being_swapped)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        other_vendor.add(self.inventory[0])
        self.remove(self.inventory[0])
        self.add(other_vendor.inventory[0])
        other_vendor.remove(other_vendor.inventory[0])  
        return True

    def get_best_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)   
        category_list.sort(key=lambda x: x.condition)  
        if not category_list:
            return None 
        return category_list[-1]

    def swap_best_by_category(self, other_vendor, my_desire, other_desire):
        if other_desire not in self.inventory or my_desire not in other_vendor.inventory:
            return False


        
        # item_being_swapped = self.remove(item_x)
        # other_vendor.add(item_being_swapped)
        # item_being_swapped = other_vendor.remove(item_y)
        # self.add(item_being_swapped)        
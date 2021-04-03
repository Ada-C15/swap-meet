class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self,category):
        category_specific_list = []
        for item in self.inventory:
            if item.category == category:
                category_specific_list.append(item)
        return category_specific_list

    def swap_items(self, Vendor, my_item, their_item):
        if my_item in self.inventory and their_item in Vendor.inventory:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            Vendor.inventory.remove(their_item)
            Vendor.inventory.append(my_item)
            return True
        else:
            return False
    
    def swap_first_item(self, Vendor):
        if len(Vendor.inventory) == 0 or len(self.inventory) == 0:
            return False
        else:
            self.inventory.append(Vendor.inventory[0])
            Vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0]) 
            Vendor.inventory.remove(Vendor.inventory[0])
            return True
    
    def get_best_by_category(self, category):
        for item in self.inventory:
            if category == item.category:
                if item.condition == max(item.condition):
                    return item.category
            else:
                return None

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
        if Vendor.inventory == [] or self.inventory == []:
            return False
        else:
            self.inventory.append(Vendor.inventory[0])
            Vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0]) 
            Vendor.inventory.remove(Vendor.inventory[0])
            return True
    
    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        initial_condition = 0.0
        best_item = None
        for item in category_items:
            if item.condition > initial_condition:
                initial_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        their_best_item = other.get_best_by_category(my_priority)
        my_best_item = self.get_best_by_category(their_priority)

        if self.inventory == [] or other.inventory == []:
            return False
        else:
            return self.swap_items(other, my_best_item, their_best_item)


from swap_meet.item import Item 

class Vendor:

    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory 

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        return items_in_category
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False
    
    def swap_first_item(self, other_vendor):        
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        else:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True

    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        if len(items_in_category) == 0:
            return None
        else:
            best_condition = 0
            for item in items_in_category:
                if item.condition >= best_condition:
                    best_condition = item.condition
                    best_item = item
            return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        vendor_priority_item = other.get_best_by_category(my_priority)
        other_priority_item = self.get_best_by_category(their_priority)
        if vendor_priority_item == None or other_priority_item == None:
            return False
        else:
            self.swap_items(other, other_priority_item, vendor_priority_item)
            return True


    #optional enhancements
    def get_newest(self):
        newest_item = None
        age_of_newest = 100000
        for item in self.inventory:
            if item.age == None:
                continue
            elif item.age < age_of_newest:
                newest_item = item
                age_of_newest = item.age
        return newest_item

    def swap_by_newest(self, other):
        if self.get_newest() == None or other.get_newest() == None:
            return False
        else:
            self.swap_items(other, self.get_newest(), other.get_newest()) 
            return True


    # consider making an "eligible to participate in swap" method to replace
    # all of the checking for len(items_list) > 0 
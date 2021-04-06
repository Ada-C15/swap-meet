from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        result = self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            result = self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, other_vendor, vendor_item, other_vendor_item):
        if vendor_item not in self.inventory or other_vendor_item not in other_vendor.inventory:
            return False
        else:
            for item in other_vendor.inventory:
                if item == other_vendor_item:
                    self.inventory.append(item)
                    other_vendor.inventory.remove(item)
            for item in self.inventory:
                if item == vendor_item:
                    other_vendor.inventory.append(item)
                    self.inventory.remove(item)
            return True

    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            self.swap_items(other_vendor,self.inventory[0],other_vendor.inventory[0])
            return True

    def get_best_by_category(self, category):
        largest_num = 0
        largest_item = None
        for item in self.inventory:
            if category == item.category:
                if item.condition > largest_num:
                    largest_num = item.condition
                    largest_item = item
        return largest_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        
        if self.inventory == [] or other.inventory == []:
            return False
        else:
            vendor_item = other.get_best_by_category(my_priority)
            other_item = self.get_best_by_category(their_priority)
            self.swap_items(other, other_item, vendor_item)

            return True
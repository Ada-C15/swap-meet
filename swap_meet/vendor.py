class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.category == category:
                result.append(item)
        return result

    def swap_items(self, other_vendor, my_item, other_item):
        if my_item not in self.inventory or other_item not in other_vendor.inventory:
            return False
        else:
            other_vendor.inventory.append(my_item)
            self.inventory.remove(my_item)
            self.inventory.append(other_item)
            other_vendor.inventory.remove(other_item)
            return True
    
    def swap_first_item(self, other):
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False

        return self.swap_items(other, self.inventory[0], other.inventory[0])

    def get_best_by_category(self, category):
        best_item = None
        best_item_condition = 0

        for item in self.inventory:
            if item.category == category:
                if item.condition > best_item_condition:
                    best_item = item
                    best_item_condition = item.condition

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item_other_wants = self.get_best_by_category(their_priority)
        their_best_item_I_want = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_best_item_other_wants, their_best_item_I_want)

    def get_newest(self):
        newest_item = self.inventory[0]
        newest_item_age = self.inventory[0].age

        for item in self.inventory:
            if item.age < newest_item_age:
                newest_item = item
                newest_item_age = item.age
        
        return newest_item

    def swap_by_newest(self, other):
        my_newest_item = self.get_newest()
        their_newest_item = other.get_newest()

        return self.swap_items(other, my_newest_item, their_newest_item)

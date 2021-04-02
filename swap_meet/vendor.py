class Vendor():
    def __init__(self, inventory = None):
        if inventory == None:
            inventory = []
        self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            item = False
        return item

    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        return items_in_category

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.append(their_item)
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.remove(their_item)
            return True
        else:
            return False

    def swap_first_item(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            # Using .pop() against Bertrand Meyer's express wishes \_('-')_/
            self.inventory.append(other_vendor.inventory.pop(0))
            other_vendor.inventory.append(self.inventory.pop(0))
            return True
        else:
            return False

    def get_best_by_category(self, category):
        best_condition = 0
        best_item = None
        for item in self.inventory:
            if item.category == category:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
            my_item = self.get_best_by_category(their_priority)
            their_item = other.get_best_by_category(my_priority)
            return self.swap_items(other, my_item, their_item)
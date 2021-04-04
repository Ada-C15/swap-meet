class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
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
        category_items = []
        for specific_item in self.inventory:
            if specific_item.category == category:
                category_items.append(specific_item)

        return category_items


    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        self.inventory.remove(my_item)
        vendor.inventory.append(my_item)
        vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True


    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
        my_first_item = self.inventory[0]
        self.inventory[0] = vendor.inventory[0]
        vendor.inventory[0] = my_first_item

        return True


    def get_best_by_category(self, category):
        items_list = []
        best_condition = 0
        for match in self.inventory:
            if match.category == category:
                items_list.append(match)
        if not items_list:
            return None
        for item in items_list:
            if item.condition > best_condition:
                best_condition = item.condition
                goodie = item

        return goodie




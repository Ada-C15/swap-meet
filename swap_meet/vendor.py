class Vendor:

    def __init__(self, inventory=[]):
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

    def get_by_category(self, category=" "):
        list_items = []
        for item in self.inventory:
            if item.category == category:
                list_items.append(item)
        return list_items

    def swap_items(self, other, my_item, their_item):
        if my_item not in self.inventory or their_item not in other.inventory:
            return False

        self.inventory.remove(my_item)
        other.inventory.append(my_item)

        self.inventory.append(their_item)
        other.inventory.remove(their_item)

        return True

    def swap_first_item(self, other):

        if len(self.inventory) < 1 or len(other.inventory) < 1:
            return False

        my_item = self.inventory[0]
        their_item = other.inventory[0]

        self.inventory.remove(my_item)
        other.inventory.append(my_item)

        self.inventory.append(their_item)
        other.inventory.remove(their_item)
        return True

        # self.swap_items(other, my_item, their_item)

    def get_best_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)

        if len(category_items) < 1:
            return None

        sorted_items = sorted(category_items, key=lambda cat: cat.condition)
        return sorted_items[-1]

    def swap_best_by_category(self, other: 'Vendor', my_priority: str, their_priority: str):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        if not my_item or not their_item:
            return False

        return self.swap_items(other, my_item, their_item)

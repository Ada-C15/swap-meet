from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        elif item in self.inventory:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        list_of_items = []
        for item in self.inventory:
            if item.category == category:
                list_of_items.append(item)
        return list_of_items

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        self.inventory.remove(my_item)
        friend.inventory.append(my_item)
        friend.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True

    def swap_first_item(self, friend):
        if (len(self.inventory) == 0) or (len(friend.inventory) == 0):
            return False

        my_first_item = self.inventory[0]
        their_first_item = friend.inventory[0]
        self.swap_items(friend, my_first_item, their_first_item)
        return True
    
    def get_best_by_category(self, category):
        pass

    def swap_best_by_category(self, other, my_priority, their_priority):
        pass


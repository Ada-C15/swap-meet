from swap_meet.item import Item
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
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if category == item.category:
                item_list.append(item)
        return item_list

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        else:
            friend.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            friend.remove(their_item)
            return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = friend.inventory[0]
            self.add(their_first_item)
            friend.remove(their_first_item)
            friend.add(my_first_item)
            self.remove(my_first_item)
            return True

    def get_best_by_category(self, category):
        if category not in self.inventory:
            return None
        #get_by_category.item_list


    def swap_best_by_category(self, other, my_priority, their_priority):
        if their_priority not in self.inventory:
            return False
        if my_priority not in other.inventory:
            return False


# test

sid = Vendor()
print(sid.inventory)

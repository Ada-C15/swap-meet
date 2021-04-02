class Vendor:
    # wave 01
    def __init__(self, inventory=None):
        self.inventory = [] if inventory == None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        for i, thing in enumerate(self.inventory):
            if thing == item:
                del self.inventory[i]
                return item

        return False

        # if item not in self.inventory:
        #     return False
        # self.inventory.remove(item)
        # return item

    # wave 02
    def get_by_category(self, category):
        items = []

        for item in self.inventory:
            if item.category == category:
                items.append(item)

        return items
    
    #  wave 03
    def swap_items(self, friend, my_item, their_item):
        my_inventory = set(self.inventory)
        friend_inventory = set(friend.inventory)

        if my_item in my_inventory and their_item in friend_inventory:
            self.inventory.remove(my_item)
            friend.inventory.append(my_item)
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            return True  

        return False

    #  wave 04
    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        else:
            friend.inventory.append(self.inventory[0])
            del self.inventory[0]
            self.inventory.append(friend.inventory[0])
            del friend.inventory[0]
            return True        

    #  wave 06
    def get_best_by_category(self, category):
        highest_condition_rate = 0.0
        best_item_by_category = None

        for item in self.inventory:
            if item.category == category and \
            item.condition >= highest_condition_rate:
                highest_condition_rate = item.condition
                best_item_by_category = item

        return best_item_by_category

    # wave 06
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_preferred_item = other.get_best_by_category(my_priority)
        their_preferred_item = self.get_best_by_category(their_priority)

        swap_result = self.swap_items(other, their_preferred_item, my_preferred_item)

        return swap_result
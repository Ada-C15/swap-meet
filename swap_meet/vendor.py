class Vendor():
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
        # self.inventory = inventory or []  

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
        picked_items = []
        for item in self.inventory:
            if item.category == category:
                picked_items.append(item)
        return picked_items

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.add(their_item)
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            return True        
        else:
            return False

    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            my_item = self.inventory[0]
            their_item = friend.inventory[0]
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if len(items) == 0:
            return None
        best = items[0]
        for item in items:
            if item.condition > best.condition:
                best = item
        return best

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        others_best_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_best_item, others_best_item)

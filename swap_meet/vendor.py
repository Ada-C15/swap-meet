# Wave 1
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
    # Wave 2
    def get_by_category(self, category):
        picked_items = []
        for item in self.inventory:
            if item.category == category:
                picked_items.append(item)
        return picked_items
    # Wave 3
    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.add(their_item)
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            return True        
        else:
            return False
    # Wave 4
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

class Vendor():
    def __init__(self, inventory = None):
        self.inventory = inventory or [] # [on_true] if [expression] else [on_false] 

    def add(self, item):
        """Adds item to an inventory"""
        self.inventory.append(item)
        return item

    def remove(self, item):
        """Removes item from an inventory"""
        if item in self.inventory: 
            self.inventory.remove(item)
            return item
        else: 
            return False        

    def get_by_category(self, category):
        """Returns a list of items within a given category"""
        picked_items = []
        for item in self.inventory:
            if item.category == category:
                picked_items.append(item)
        return picked_items

    def swap_items(self, friend, my_item, their_item):
        """
        - Removes an item from Instances' inventory, adds it to a Friend's inventory
        - Removes Friends item from a Friend's inventory, adds it to Instances' inventory
        """
        if my_item in self.inventory and their_item in friend.inventory:
            self.add(their_item)
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            return True        
        else:
            return False

    def swap_first_item(self, friend):
        """
        Removes the first item from Instances' inventory, adds Friend's first item
        Removes the first item from Friend's inventory, adds Instances first item
        """
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        return self.swap_items(friend, self.inventory[0], friend.inventory[0])

    def get_best_by_category(self, category):
        """Returns highest rated item in a given category"""
        items = self.get_by_category(category)
        if len(items) == 0:
            return None
        best_item = items[0]
        for item in items:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """Swaps highest rated items within a given category"""
        my_best_item = self.get_best_by_category(their_priority)
        others_best_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_best_item, others_best_item)

    def get_newest_by_category(self, category):
        """Returns newest item in a given category"""
        items = self.get_by_category(category)
        if len(items) == 0:
            return None
        newest_item = items[0]
        for item in items:
            if item.age < newest_item.age:
                newest_item = item
        return newest_item

    def swap_newest_by_category(self, friend, age, category):
        """Swaps newest items within a given category"""
        newest_item = self.get_newest_by_category(category)
        friend_newest_item = friend.get_newest_by_category(category)

        return self.swap_items(friend, newest_item, friend_newest_item)
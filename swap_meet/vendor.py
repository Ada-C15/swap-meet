#wave 1
class Vendor: 
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, remove_item):
        if remove_item not in self.inventory:
            return False
        else:
            self.inventory.remove(remove_item)
            return remove_item
    
    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list

#Wave 3
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or \
            their_item not in friend.inventory:
            return False

        self.remove(my_item)
        friend.add(my_item)
        friend.remove(their_item)
        self.add(their_item)

        return True

#Wave 4
    def swap_first_item(self, friend):
        if  len(self.inventory) < 1 or \
                len(friend.inventory) < 1:
            return False
        my_first_item = self.inventory[0]
        their_first_item = friend.inventory[0]
        self.swap_items(friend, my_first_item, their_first_item)
        return True 
        
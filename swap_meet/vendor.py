from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
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

#Wave 2
    def get_by_category(self, category):
        list_of_items_in_category = []
        for item in self.inventory:
            if category == item.category:
                list_of_items_in_category.append(item)
        return list_of_items_in_category

#Wave 3
    def swap_items(self, friend, item, friend_item):
        if item not in self.inventory or friend_item not in friend.inventory:
            return False
        else:
            self.remove(item)
            friend.add(item)
            self.add(friend_item)
            friend.remove(friend_item)
            return True  
#Wave 4
    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False 
        else:
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True

#Wave 6
    def get_best_by_category(self, category):
        all_items_in_category = self.get_by_category(category)
        best_item = None
        best_item_condition = 0.0
        if all_items_in_category == []:
            return None
        
        for item in all_items_in_category:
            if item.condition > best_item_condition:
                best_item_condition = item.condition
                best_item = item
        return best_item
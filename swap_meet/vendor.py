
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
        if item in self.inventory:
            self.inventory.remove(item)
            return item
    
    def get_by_category(self, category):
        matching_items = [] 
        for item in self.inventory:
            if category == item.category:
                matching_items.append(item)

        return  matching_items
    
    def swap_items(self, friend, my_item, friends_item):
        if my_item in self.inventory and friends_item in friend.inventory:
            # friend.add(self.remove(my_item))
            # self.add(friend.remove(friends_item))
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(friends_item)
            self.add(friends_item)                 
            return True
        else:
            return False



    def swap_first_item(self, friend):

        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        else:
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True

    def get_best_by_category(self, category):
        list_of_categorys = self.get_by_category(category)
        if not list_of_categorys: 
            return None
        top_condition = -1
        top_item = None
        for item in list_of_categorys:
            if item.condition > top_condition:
                top_condition = item.condition
                top_item = item
        return top_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        item_for_other = self.get_best_by_category(their_priority)
        item_for_self = other.get_best_by_category(my_priority)
        if item_for_other and item_for_self:
            self.swap_items(other, item_for_other, item_for_self)
            return True
        else:
            return False
        
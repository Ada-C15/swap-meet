class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory 
    
    def add(self, item):
        (self.inventory).append(item) 
        return item

    def remove(self, item): 
        item_index = None
        for index in range(len(self.inventory)):
            if item == self.inventory[index]:
                return self.inventory.pop(index)
        return False

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category] 
    
    def swap_items(self, friend_vendor, my_item, their_item):
        friend_list = friend_vendor.inventory  
        my_list = self.inventory  
        if their_item in friend_list and my_item in my_list \
            and their_item != None and my_item != None and my_list != []\
            and friend_list !=[]:
            their_removed = friend_vendor.remove(their_item)
            my_removed  = self.remove(my_item) 
            friend_list.append(my_removed)
            my_list.append(their_removed)
            return True
        else:
            return False

    def swap_first_item(self, friend_vendor):
        friend_list = friend_vendor.inventory  
        my_list = self.inventory 
        if  my_list != [] and friend_list !=[]:
            their_removed = friend_vendor.remove(friend_list[0])
            my_removed  = self.remove(self.inventory[0]) 
            friend_list.append(my_removed)
            my_list.append(their_removed)
            return True
        else:
            return False   

    def get_best_by_category(self, category):
        items_by_category = self.get_by_category(category)
        if len(items_by_category) == 0:
            return None
        
        best_item = items_by_category[0]
        for item in items_by_category:
            if best_item.condition < item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, \
        their_priority):
        my_item = self.get_best_by_category(their_priority)  
        their_item = other.get_best_by_category(my_priority) 
        swap = self.swap_items(other, my_item, their_item)
        return swap

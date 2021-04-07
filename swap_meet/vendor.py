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

        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):

        matching_items = []
        for item in self.inventory:
            if item.category == category:
                matching_items.append(item)
        return matching_items


    def swap_items(self, vendor_friend, my_item, their_item):

        if my_item not in self.inventory or their_item not in vendor_friend.inventory: 
            return False 
        else:
            self.remove(my_item)
            vendor_friend.add(my_item)
            vendor_friend.remove(their_item)
            self.add(their_item)
            return True


    def swap_first_item(self, vendor_friend):

        if self.inventory and vendor_friend.inventory:
            my_item = self.inventory[0]
            their_item = vendor_friend.inventory[0]
            self.swap_items(vendor_friend, my_item, their_item)
            return True
        else:
            return False

    def get_best_by_category(self, category):

        list_of_items = self.get_by_category(category)

        for item in list_of_items:
            if list_of_items == []:
                return None
        
        best_condition = 0.0
        for item in list_of_items:
            if item.condition > best_condition:
                best_condition = item.condition
        for item in list_of_items:
            if best_condition == item.condition:
                return item 

    def swap_best_by_category(self, other, my_priority, their_priority):
        
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if their_best_item == None or my_best_item == None:
            return False
        else: 
            return self.swap_items(other, my_best_item, their_best_item)

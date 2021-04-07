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
        category_list =[]
        for items in self.inventory:
            if items.category == category:
                category_list.append(items)
        return category_list

#Wave 3 *****************************

    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend_vendor.inventory:
            return False
        self.remove(my_item)
        friend_vendor.add(my_item)
        friend_vendor.remove(their_item)
        self.add(their_item)
        return True


#Wave 4 **********************************

    def swap_first_item(self, friend):
        
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        first_item = self.inventory[0]
        self.remove(self.inventory[0])
        self.add(friend.inventory[0])
        friend.remove(friend.inventory[0])
        friend.add(first_item)
        
        return True

#Wave 6 ***************************

    def get_best_by_category(self, category):
        highest_condition = 0
        highest_item = None
        for item in self.inventory:
            if item.category == category:
                if item.condition > highest_condition:
                    highest_condition = item.condition
                    highest_item = item
        return highest_item


    def swap_best_by_category(self, other, my_priority, their_priority):
        best_in_my_inventory = self.get_best_by_category(their_priority)
        best_item_in_other = other.get_best_by_category(my_priority)
        if best_item_in_other == None or best_in_my_inventory == None:
            return False
        self.swap_items(other, best_in_my_inventory, best_item_in_other)
        return True
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
        friend = [their_item]
        if my_item in self.inventory and their_item in friend:
            self.inventory.remove(my_item)
            friend.append(my_item)
            self.inventory.remove(their_item)
            friend_vendor.inventory.append(their_item)
            return True
        else:
            return False


#Wave 4 **********************************

    def swap_first_item(self, friend):
        friends_first = friend.inventory[0]
        first = self.inventory[0]
        if len(self.inventory) > 0 and len(friend.inventory) > 0:
            self.inventory.remove(first)
            friend.inventory.append(first)
            friend.inventory.remove(friends_first)
            self.inventory.append(friends_first)
            return True
        else:
            return False



#Wave 5 ***************************
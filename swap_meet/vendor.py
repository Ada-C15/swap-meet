

class Vendor:
    def __init__(self, inventory=None): #needs to be optional keyword arg
        #inventory is a list
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item): #can this function be called remove?
        if item not in self.inventory:
            return False 
        if item in self.inventory:
            self.inventory.remove(item)#if I use the remove method
            return item
    
    def get_by_category(self, types_of_items):
        matching_items = [] #this method returns a list of Items in inventory w that catego
        for item in self.inventory:
            if types_of_items == item.category:
                matching_items.append(item)

        return  matching_items
    
    def swap_items(self, friend, my_item, friends_item):
        if my_item in self.inventory and friends_item in friend.inventory:
            friend.add(self.remove(my_item))
            self.add(friend.remove(friends_item))
            # self.inventory.remove(my_item)
            # friend.inventory.add(my_item)
            # friend.inventory.remove(friends_item)
            # self.inventory.add(friends_item)                 
            return True
        else:
            return False


    #     add my_item to friends inventory (and friend is just another Vendor instance)
    #     remove friends_item from friends inventory, and add to my inventory
    #     return True if it does all this
    #     else False 
    # def swap_first_item(self, friend):
    #     if not self.inventory or not friend.inventory:
    #         return False
    #     look at the first item in self.inventory and look at the first in friend.inventory
    #     remove the first item [0] from self.inventory and add that item to friend.inventory
    #     remove the first item from friend inventory and add self inventory first item
    #     return True
    #     else false
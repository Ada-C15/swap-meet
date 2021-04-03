#from .item import Item
#from item import Item

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
            # friend.add(self.remove(my_item))
            # self.add(friend.remove(friends_item))
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(friends_item)
            self.add(friends_item)                 
            return True
        else:
            return False


    #     add my_item to friends inventory (and friend is just another Vendor instance)
    #     remove friends_item from friends inventory, and add to my inventory
    #     return True if it does all this
    #     else False 


    def swap_first_item(self, friend):
    #     if not self.inventory or not friend.inventory:

        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        else:
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True

        
        # if self.inventory and friend.inventory: 
        #     print(self)
        #     print(friend)
        #     friend.add(self.remove([0]))
        #     print(friend.inventory)
        #     self.add(friend.remove([0]))
        #     print(friend.add(self.remove([0])))
        #     return True


 
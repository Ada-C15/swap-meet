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
    
    def get_by_category(self, category):
        matching_items = [] #this method returns a list of Items in inventory w that catego
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
    #if no items in inventory matched the passed in category, return none
        if len(list_of_categorys) == 0: #if not list_of categorys
            return None
        top_condition = -1
        top_item = None
        for item in list_of_categorys:
            if item.condition > top_condition:
                top_condition = item.condition
                top_item = item
        return top_item


    #Look through self.inventory. for items with matching category.If item is highest value, like 5
    #account for duplicate items
    # return a single item. 




 
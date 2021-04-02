from .item import Item

'''
Wave 1
'''
class Vendor:

    def __init__(self, inventory = None):
        if inventory is None:
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
    '''
    Wave 2

    This method returns a list of Items in the inventory with that category
    '''
    def get_by_category(self, category):

        result = filter(lambda x: (x.category == category), self.inventory)
        return(list(result))

        # return [item for item in self.inventory if item.category == category]
    
        # if item.category == category:
        #     self.remove(item)

    '''
    Wave 3

    This method swap my item with a friend's item
    '''
    def swap_items(self, friend, my_item, their_item):

        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        else:
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            self.add(their_item)
            return True

    '''
    Wave 4

    This method swap my first item with a friend's first item
    '''
    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        # if self.invetory == None or friend.invetory == None:
        #     return False
        else:
            return self.swap_items(friend, self.inventory[0], friend.inventory[0])
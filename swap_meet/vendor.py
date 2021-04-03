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

        result = filter(lambda item: (item.category == category), self.inventory)
        return(list(result))

        # return [item for item in self.inventory if item.category == category]

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
        # if not self.inventory or not friend.inventory:
        #     return False
        if self.inventory == [] or friend.inventory == []:
            return False
        else:
            return self.swap_items(friend, self.inventory[0], friend.inventory[0])

    '''
    Wave 6

    This method gets the item with the highest condition and matching category
    '''
    def get_best_by_category(self, category):

        if not self.get_by_category(category):
            return None
        else:
            items = self.get_by_category(category) # this returns a list of items in the inventory with that matching category
            
            cur_max = items[0].condition
            cur_idx = 0

            for i in range(len(items)):
                if items[i].condition > cur_max:
                    cur_max = items[i].condition
                    cur_idx = i
            return items[cur_idx]

            # Another working solution:
            # condition_list = []
            
            # for item in items: 
            #     condition_list.append(item.condition)
       
            # max_condition = (max(condition_list))

            # for item in items:
            #     if item.condition == max_condition:
            #         return item  

            # Working solution with lambda:
            # return max(items, key=lambda item: item.condition)
            # Source: https://realpython.com/python-lambda/
    
    '''
    This method swaps the best item of certain categories with another Vendor
    '''
    def swap_best_by_category(self, other, my_priority, their_priority):

        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        
        if not my_item or not their_item:
            return False
        else:
            self.swap_items(other, my_item, their_item)
            return True




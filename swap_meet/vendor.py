import sys

class Vendor:
    # wave 01
    def __init__(self, inventory=None):
        self.inventory = [] if inventory == None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        for i, thing in enumerate(self.inventory):
            if thing == item:
                return self.inventory.pop(i)

        return False

    # wave 02
    def get_by_category(self, category):
        items = []

        for item in self.inventory:
            if item.category == category:
                items.append(item)

        return items
    
    #  wave 03
    def swap_items(self, friend, my_item, their_item):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False

        if my_item in self.inventory and their_item in friend.inventory:
            friend.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            friend.remove(their_item)
            return True  

        return False

    #  wave 04
    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
            
        return self.swap_items(friend, self.inventory[0], friend.inventory[0])    

    #  wave 06
    def get_best_by_category(self, category):
        highest_condition_rate = 0.0
        best_item_by_category = None

        for item in self.inventory:
            if item.category == category and \
            item.condition >= highest_condition_rate:
                highest_condition_rate = item.condition
                best_item_by_category = item

        return best_item_by_category

    # wave 06
    def swap_best_by_category(self, other, my_priority, their_priority):
        their_best_offer = other.get_best_by_category(my_priority)
        my_best_offer = self.get_best_by_category(their_priority)

        swap_result = self.swap_items(other, my_best_offer, their_best_offer)

        return swap_result

    # optional wave 07
    def get_min_age(self):
        """[summary]
            find a item has the mininum age in self.inventory list
        Returns:
            [type]: an object or None
        """        
        newest_item = None
        min_age = sys.maxsize

        for item in self.inventory:
            if item.age <= min_age:
                newest_item = item
                min_age = item.age
        
        return newest_item

    def swap_by_newest(self, other): 
        """[summary]
            swap min age items in inventory list of two vendor instances 
        Args:
            other ([type: object]): a Vendor instant contians inventory list

        Returns:
            [type: bool]: return true if two min age items have been swapped 
                        otherwise return false
        """           
        my_newest = self.get_min_age()
        their_newest = other.get_min_age()

        return self.swap_items(other, my_newest, their_newest) 

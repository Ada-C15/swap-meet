from swap_meet.item import Item
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.clothing import Clothing
class Vendor:

    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        '''Adds item to instance's inventory'''
        self.inventory.append(item)
        return item

    def remove(self, item):
        '''Removes item from instance's inventory'''
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        '''
        Returns list of items from instance's inventory
        that match provided category
        '''
        item_list = []
        for item in self.inventory:
            if category == item.category:
                item_list.append(item)
        return item_list

    def swap_items(self, friend, my_item, their_item):
        '''
        Swaps provided Item instance from user's inventory with provided
        Item instance from another user's inventory
        '''
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        else:
            friend.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            friend.remove(their_item)
            return True

    def swap_first_item(self, friend):
        '''
        Utilizes swap_items method to exchange first items of user's and
        friend's inventories
        '''
        if not self.inventory or not friend.inventory:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = friend.inventory[0]
            self.swap_items(friend, my_first_item, their_first_item)
            return True

    def get_best_by_category(self, category):
        '''
        Utilizes get_by_category to return Item instance in user's inventory
        that matches provided category and has highest condition rating
        '''
        list_by_category = self.get_by_category(category)
        if list_by_category == []:
            return None
        else:
            best_item = list_by_category[0]
        for item in list_by_category:
            if item.condition >= best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Utilizes best_by_category and swap_items to exchange Item
        instances of a particular category with the best condition
        between user and friend
        '''
        my_list_by_category = self.get_by_category(their_priority)
        their_list_by_category = other.get_by_category(my_priority)
        if my_list_by_category == [] or their_list_by_category == []:
            return False
        else:
            my_item = self.get_best_by_category(their_priority)
            their_item = other.get_best_by_category(my_priority)
            self.swap_items(other, my_item, their_item)
            return True

    def get_newest(self):
        '''
        Returns Item instance with the lowest age from the user's inventory
        '''
        if self.inventory == []:
            return None
        newest_item = self.inventory[0]
        for item in self.inventory:
            if item.age < newest_item.age:
                newest_item = item
        return newest_item

    def swap_by_newest(self, other):
        '''
        Utilizes get_newest and swap_items to exchange the newest item
        from user's and friend's inventories
        '''
        my_item = self.get_newest()
        their_item = other.get_newest()
        self.swap_items(other, my_item, their_item)
        return True

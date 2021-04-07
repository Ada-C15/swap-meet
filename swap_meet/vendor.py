# import pytest
# # from swap_meet.item import Item
# from swap_meet.clothing import Clothing
# from swap_meet.decor import Decor
# from swap_meet.electronics import Electronics


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.item = item
        self.inventory.append(item)
        return item

    def remove(self, item):
        self.item = item
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

# ***WAVE 2***

    def get_by_category(self, category):
        items_matching_category = []
        for item in self.inventory:
            if category == item.category:
                items_matching_category.append(item)
        return items_matching_category

# ***WAVE 3***

    def swap_items(self, Vendor, my_item, their_item):
        if (my_item in self.inventory) and (their_item in Vendor.inventory):
            self.remove(my_item)
            self.add(their_item)
            Vendor.add(my_item)
            Vendor.remove(their_item)
            return True
        return False

# ***WAVE 4***
    def swap_first_item(self, Vendor):
        if (self.inventory and Vendor.inventory):
            return self.swap_items(Vendor, self.inventory[0], Vendor.inventory[0])
        return False


#  ***WAVE 6***

        # max((item.value for item in categories_list))

# def get_by_category(self, category):
#     items_matching_category = []
#     for item in self.inventory:
#         if category == item.category:
#             items_matching_category.append(item)
#     return items_matching_category


    def get_best_by_category(self, category):
        list = []
        for item in self.get_by_category(category):
            list.append(item.condition)
        for item in self.get_by_category(category):
            if item.condition == max(list):
                return item

    def swap_best_by_category(self, other, my_priority, their_priority):

        if (my_priority in self.inventory) and (their_priority in other.inventory):
            self.swap_items(other, self.get_best_by_category(
                my_priority), other.get_best_by_category(their_priority))
            return True
        return False

        # if (my_priority in self.condition) and (their_priority in Vendor.condition):
        #     get_best_by_category(my_priority)
        #     get_best_by_category(their_priority)

        # def swap_items(self, Vendor, my_item, their_item):
        #     if (my_item in self.inventory) and (their_item in Vendor.inventory):
        #         self.remove(my_item)
        #         self.add(their_item)
        #         Vendor.add(my_item)
        #         Vendor.remove(their_item)
        #         return True
        #     return False

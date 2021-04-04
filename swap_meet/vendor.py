# Swap Meet
# Ada Cohort 15 - Paper
# Katrina Kimzey (she|they)
# Started March 31, 2021

class Vendor:
    def __init__(self, inventory = None):
        # include an inventory
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
        

    def add(self, item):
        # inventory entry
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
        except ValueError as err:
            return False

        return item

    def get_by_category(self, category):
        category_matches = []

        for item in self.inventory:
            if item.category == category:
                category_matches.append(item)

        return category_matches

    def swap_items(self, friend, my_item, their_item):
        if (my_item in self.inventory and 
            their_item in friend.inventory):
            self.remove(my_item)
            friend.remove(their_item)
            self.add(their_item)
            friend.add(my_item)
            return True
        else:
            return False
        

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
        
    def swap_first_item(self, friend):
        if len(self.inventory) and len(friend.inventory):
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True
        else:
            return False

    def get_best_by_category(self, category):
        items_of_category = self.get_by_category(category)

        if items_of_category == []:
            return None
        
        best_item = items_of_category[0]

        for item in items_of_category:
            if best_item.condition < item.condition:
                best_item = item

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        mine_to_swap = self.get_best_by_category(their_priority)
        theirs_to_swap = other.get_best_by_category(my_priority)

        if mine_to_swap and theirs_to_swap:
            self.swap_items(other, mine_to_swap, theirs_to_swap)
            return True
        else:
            return False

    def swap_by_newest(self, other):
        if len(self.inventory) and len(other.inventory):
            mine_to_swap = self.inventory[0]
            theirs_to_swap = other.inventory[0]

            for my_item in self.inventory:
                if mine_to_swap.age > my_item.age:
                    mine_to_swap = my_item

            for their_item in other.inventory:
                if theirs_to_swap.age > their_item.age:
                    theirs_to_swap = their_item

            self.swap_items(other, mine_to_swap, theirs_to_swap)
            return True
        else:
            return False
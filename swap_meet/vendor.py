
class Vendor:

    def __init__(self, inventory= None):
        if inventory == None:
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
    

    def get_by_category(self, category):
        cat_list = []
        for item in self.inventory:
            if item.category is category:
                cat_list.append(item)
        return cat_list
        #return [item for item in self.inventory if item.category == category]


    def swap_items(self, other, my_item, their_item):
        if my_item in self.inventory and their_item in other.inventory:
            self.remove(my_item)
            other.add(my_item)
            self.add(their_item)
            other.remove(their_item)
            return True
        else:
            return False


    def swap_first_item(self, other):
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = other.inventory[0]
            self.swap_items(other, my_first_item, their_first_item)
            return True


    def get_best_by_category(self, category):
        items_list = self.get_by_category(category)
        if len(items_list) == 0:
            return None

        best_condition_item = items_list[0]
        for item in items_list:
            if item.condition > best_condition_item.condition:
                best_condition_item = item
        return best_condition_item
#[for item in items_list if item.condition > best_condition_item.condition]


    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        if my_item and their_item:
            self.swap_items(other, my_item, their_item)
            return True
        else:
            return False        



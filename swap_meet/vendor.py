# from item import Item 

class Vendor:

    def __init__(self, inventory = []):
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
        self.category = category
        category_list = []

        for item in self.inventory:

            if item.category == category:
                category_list.append(item)

        return category_list

    def swap_items(self, other, my_item, their_item):
        
        self.other = other
        self.my_item = my_item
        self.their_item = their_item

        if my_item == True and their_item == True:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            other.inventory.append(my_item)
            other.inventory.remove(their_item)
            return self.inventory, bool(self.inventory)

        else:
            return False

    def swap_first_item(self, other):

        self.other = other

        if len(self.inventory) > 0 and len(other.inventory) > 0:
            my_first_item = self.inventory[0]
            their_first_item = other.inventory[0]

            self.inventory[0] = their_first_item
            other.inventory[0] = my_first_item
            return bool(self.inventory)

        else:
            return False

    def get_best_by_category(self, category):
        
        best_in_category = []

        for item in self.inventory:
            if item.category == category:
                best_in_category.append(item)

        for item in best_in_category:
            if item.category == category:
                for condition in best_in_category:
                    if item.condition == 5.0:
                        return item
                    elif item.condition == 4.0:
                        return item
                    elif item.condition == 3.0:
                        return item
                    elif item.condition == 2.0:
                        return item
                    elif item.condition == 1.0:
                        return itme 
            else:
                return None
    
    def swap_best_by_category(self, other, my_priority, their_priority):
    
        if my_priority not in other.inventory or their_priority not in self.inventory:
            return False
        else:
            return True 






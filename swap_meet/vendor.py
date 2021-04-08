
class Vendor:

    def __init__(self, inventory=None):
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
        category_list = []
        for item in self.inventory:
            if category == item.category:
                category_list.append(item)
        return category_list

    def swap_items(self, other_vendor, my_item, their_item):
        
        if their_item not in other_vendor.inventory or my_item not in self.inventory:

            return False     

        else:

            other_vendor.inventory.append(my_item)
            other_vendor.remove(their_item)
            self.inventory.remove(my_item)
            self.inventory.append(their_item)

            return True
    
    def swap_first_item(self, other_vendor):


        if self.inventory == [] or other_vendor.inventory == []:

            return False

        else:

            other_vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            self.inventory.append(other_vendor.inventory[0])
            other_vendor.inventory.remove(other_vendor.inventory[0])

            return True

    def get_best_by_category(self, category=""):
        items_in_category = []

        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        
        best_item = None
        best_condition = 0
        for item in items_in_category:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item
        

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        return self.swap_items(other, my_best, their_best)
        

            







        
    
                

        



        

        
        
        



        

        
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
    #be careful of functions returning more than one type. 

    def get_by_category(self, category):
        categorized_items =[]
        for item in self.inventory:
            if item.category is category:
                categorized_items.append(item)
        return categorized_items

    def swap_items(self, vendor, my_item, their_item):
        if their_item in vendor.inventory and my_item in self.inventory:
            self.remove(my_item)
            vendor.remove(their_item)
            self.add(their_item)
            vendor.add(my_item)
            return True
        else:
            return False

    def swap_first_item(self, vendor):
        if self.inventory and vendor.inventory != []:
            my_item = self.inventory[0]
            their_item = vendor.inventory[0]
            self.remove(my_item)
            vendor.remove(their_item)
            self.add(their_item)
            vendor.add(my_item)
            return True
        else:
            return False
    
    def get_best_by_category(self, category):
        if self.inventory == []:
            return None
        categorized_items = self.get_by_category(category)
        best_condition = 0
        best_item = None
        for item in categorized_items:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item
        
    def swap_best_by_category(self, other, my_priority, their_priority):

        my_list = other.get_by_category(my_priority)
        their_list = self.get_by_category(their_priority)

        if their_list == [] or my_list == []:
            return False

        they_want = self.get_best_by_category(their_priority)
        my_want = other.get_best_by_category(my_priority)

        self.swap_items(other, they_want, my_want) 
        
        return True



        

    
        
from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None): 
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
        result = []
        for item in self.inventory: 
            if item.category == category: 
                result.append(item)

        return result
    

    def swap_items(self, vendor, item_1, item_2):
        if item_1 not in self.inventory or item_2 not in vendor.inventory:
            return False
        
        found = False
        for item in self.inventory:
            if item == item_1:
                self.inventory.remove(item)
                vendor.inventory.append(item)
                found = True

        if not found:
            return False

        found = False
        for item in vendor.inventory:
            if item == item_2:
                vendor.inventory.remove(item)
                self.inventory.append(item)
                found = True
        
        return found


    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False

        self.inventory.append(vendor.inventory.pop(0))
        vendor.inventory.append(self.inventory.pop(0))

        return True
        
    def get_best_by_category(self, category):

        matched_categories = []
        for item in self.inventory:
            if item.category == category:
                matched_categories.append(item)
        
        if not matched_categories:
            return None

        best_item = ""
        highest_condition = 0
        for item in matched_categories:
            if item.condition > highest_condition:
                highest_condition = item.condition
                best_item = item
        return best_item


        



class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else: 
            self.inventory = inventory 
        
    def adding_to_inventory(Vendor): #checks item in inventory & returns True or False 
        if item in inventory:
            self.inventory.add(item)
        else:
            self.inventory.remove(item)
        return False 
    
    def add(self, item): #append item in inventory 
        self.inventory.append(item)
        return item

    def remove(self, item): #remove item from inventory
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False 
            
        return item 

    def get_by_category(self, category):
        """
        gets items by category
        input: inventory from items
        output: list of category 

        """
        item_by_category = []
        for item in self.inventory:
            if item.category == category:
                item_by_category.append(item)
        return item_by_category


    def swap_items(self, vendor, my_item, their_item):
        """
        check items in Vendor, my_item, their_item
        input:
        output: 
        """
        for item in self.inventory:
            if item == my_item:
                self.remove(item)
                vendor.add(item)
                if their_item not in vendor.inventory:
                    return False 
                else: 
                    self.add(their_item)
                    vendor.remove(their_item)
                    return True
            else: 
                return False
        return False 





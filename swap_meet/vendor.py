from .item import Item


class Vendor: 
    """
    Define a class that can keep inventory 
    """
    def __init__(self, inventory = None):
        if inventory == None:
                self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        """
        Takes in an item and adds it to the Vendor objects inventory attribute
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        """
        Takes in an item and removes it from the Vendor objects invntry attribute
        """
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        return item 
    
    def get_by_category(self, category):
        """
        Takes in a preferred category and returns all items in vendor 
        inventory that match that category
        """
        item_by_category = []
        for item in self.inventory:
            if item.category == category:
                item_by_category.append(item)
        return item_by_category

    def swap_items(self, vendor, item_a, item_b):
        """
        Takes in an instance of vendor, and two instances of items:
        checks to see if the items are in the respective .inventory 
        attributes and removes/adds them if they are
        """
        if item_a in self.inventory and item_b in vendor.inventory:
            self.remove(item_a)
            vendor.add(item_a)
            self.add(item_b)
            vendor.remove(item_b)
        else: 
            return False
        return True
    
    def swap_first_item(self, vendor):
        """
        Takes in an instance of vendor and compares inventory lists, 
        swaps first item of each list if the list contains >= 1 item
        """
        if len(self.inventory) >= 1 and len(vendor.inventory)>= 1:
            self_first_item = self.inventory[0]
            vendor_first_item = vendor.inventory[0]
        else:
            return False
        self.swap_items(vendor, self_first_item, vendor_first_item)
        return True

    def get_best_by_category(self, category):
        """
        Takes in a category and iterates over item instances in 
        self.inventory, returns item in best condition 
        """
        best_condition = 0
        best_item = None
        for item in self.inventory:
            if item.category == category:
                if item.condition >= best_condition:
                    best_condition += item.condition
                    best_item = item    
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Makes use of the best by category funct. for self and other vendor 
        based off of the category priorities passed in. 
        swaps items from respective inv. lists if they are present
        """
        self_wants = other.get_best_by_category(my_priority)

        vendor_wants = self.get_best_by_category(their_priority)
        if vendor_wants == None or self_wants == None:
            return False
        else:
            self.swap_items(other, vendor_wants, self_wants)
            return True

    def get_newest(self):
        """
        iterates over item objects in self.inventory and returns item 
        with the youngest age in (int)
        """
        best_age = 999999
        best_item = None
        for item in self.inventory:
            if item.age == None:
                return False
            if item.age < best_age:
                best_age = item.age
                best_item = item
        return best_item

    def swap_best_by_age(self, other):
        """
        Makes use of the get newest funct for self and other, then 
        swaps the return items if they are present. 
        """
        self_wants = other.get_newest()
        vendor_wants = self.get_newest()
        if self_wants == None or vendor_wants == None:
            return False
        else:
            self.swap_items(other, vendor_wants, self_wants)

        return True



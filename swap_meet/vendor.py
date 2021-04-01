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
        items_list = []
        for item in self.inventory:
            if item.category == category:
                print(f"The item.category is {item.category}")
                items_list.append(item)
        print(f"The item list is {items_list}")
        return items_list
    
    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item) # removes my_item from the main vendor's inventory
            vendor.inventory.append(my_item) # adds my_item to the vendor friend inventory
            vendor.inventory.remove(their_item) # removes their_item from the vendor friend's inventory
            self.inventory.append(their_item) # adds their_item to the main vendor's inventory
            return True
        else:
            return False

      
 

    
    
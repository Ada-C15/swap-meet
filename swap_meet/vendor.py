# WAVE ONE

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
        items_by_category = []
        for item in self.inventory:
            if item.category == category:
                items_by_category.append(item)
        return items_by_category 

    def swap_items(self, vendor_friend, my_item, their_item):
        if my_item not in vendor_friend.inventory and my_item in self.inventory and their_item in vendor_friend.inventory and their_item not in self.inventory:
            self.remove(my_item)
            vendor_friend.add(my_item)
            vendor_friend.remove(their_item)
            self.add(their_item)
            return True  
        else:
            return False 


        # for item in self.inventory:
        #     if item in self.inventory and item in vendor_friend.inventory:
        #         self.inventory.remove(item)
        #         vendor_friend.inventory.add(item)
        #         return True
        #     else:
        #         return False 
    

        # for item in vendor_friend.inventory:
        #     if item == my_item:
        #         vendor_friend.inventory.remove(item)
        #         self.inventory.add(item) 
        #         return True  
        #     else:
        #         return False 
    
    
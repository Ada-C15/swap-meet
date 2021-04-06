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
    
    def get_by_category(self, category = ""):
        item_list = []
        for item in self.inventory:
            if category == item.category:
                item_list.append(item)
        return item_list
    
    def swap_items(self, vendor_friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor_friend.inventory:
            return False
        else:
            self.remove(my_item)
            vendor_friend.add(my_item)
            vendor_friend.remove(their_item)
            self.add(their_item)
            return True
    
    def swap_first_item(self, vendor_friend):
        if self.inventory and vendor_friend.inventory:
            my_item = self.inventory[0]
            their_item = vendor_friend.inventory[0]
            self.swap_items(vendor_friend, my_item, their_item)
            return True
        else: 
            return False
    
    def get_best_by_category(self, category):
        product = []
        for item in self.inventory:
            if item.category == category:
                product.append(item)
        if not product:
            return None
        
        result = product[0]
        for item in product:
            if item.condition > result.condition:
                result = item
        return result

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        if not my_item:
            return False
        if not their_item:
            return False
        
        self.swap_items(other, my_item, their_item)
        return True 
        


        
            
            
    


            
        

            
            

    

    













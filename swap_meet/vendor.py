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
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list
    
    
    

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        self.remove(my_item)
        friend.add(my_item)
        
        friend.remove(their_item)
        self.add(their_item)
        return True



    def swap_first_item(self, friend):
        
        if len(self.inventory) <= 0 or len(friend.inventory) <= 0:
            return False

        my_first_item = self.inventory[0]
        
        friend_first_item = friend.inventory[0]   
        
        self.swap_items(friend, my_first_item, friend_first_item)
        return True
    
    def get_best_by_category(self, category):
        
        best_item = None
        highest_condition = 0
        for item in self.get_by_category(category):
            if item.condition > highest_condition:
                highest_condition = item.condition
                best_item = item
        return best_item
            
                

    def swap_best_by_category(self, other, my_priority,their_priority):
        my_item_to_swap = self.get_best_by_category(their_priority)
        their_item_to_swap = other.get_best_by_category(my_priority)

        if their_item_to_swap == None or my_item_to_swap == None:
            return False


        self.swap_items(other, my_item_to_swap, their_item_to_swap)
        return True



        
        
        
        
        
        
        
        
        
        
        
        
        
    

        
                




        
        
        
        
        

    

        



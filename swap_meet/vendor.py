from swap_meet.item import Item


class Vendor:
   
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    def add(self,item):
        """ Adds item to inventory if item not 
        in inventory """

        if item not in self.inventory:
            self.inventory.append(item)
            return item
    
    def remove(self,item):
        """Removes item from inventory if 
        item in inventory """
        if item in self.inventory:
            self.inventory.remove(item)
            
            return item
    
        return False
    
    def get_by_category(self,category):
        """Takes in cateogry in string form and
        returns a list of items from inventory
        that fall under that category """

        category_list=[]
        
        for item in self.inventory:
            if item.category==category:
                category_list.append(item)

        return category_list

    def swap_items(self,friend,item_b,item_d):
        """ Swaps items between Self and friend's inventory"""

        if item_b in self.inventory and item_d in friend.inventory:
            self.inventory.remove(item_b)
            friend.inventory.append(item_b)
            friend.inventory.remove(item_d)
            self.inventory.append(item_d)
        
            return True
     
        return False


    def swap_first_item(self,friend):
        """ Swaps first item between self and friend's inventory if both inventories are not empty"""
        if self.inventory != [] and friend.inventory != []:
            self.swap_items(friend,self.inventory[0],friend.inventory[0])
            
            return True
    
        return False


    def get_best_by_category(self,category):
        """ Obtains best item from inventory that falls under select category """
      
        i_list=[]
        for object in self.get_by_category(category):
            i_list.append(object.condition)
        for object in self.get_by_category(category):
            if object.condition==max(i_list):
                return object
    
    
    def swap_best_by_category(self,other,my_priority,their_priority):
        """ Swaps item between self and other vendor, each item
         will fall under the corresponding category that each user prioritizes. The items swapped will be the ones in best conditions"""
        
        if self.get_by_category(their_priority) != [] and other.get_by_category(my_priority) != []:
            self.swap_items(other,self.get_best_by_category(their_priority),other.get_best_by_category(my_priority))  
            return True
     
        return False
            
            
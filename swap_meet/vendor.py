from swap_meet.item import Item


class Vendor:
    #useful for setting an initial value to a paramter
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    def add(self,item):
        if item not in self.inventory:
            self.inventory.append(item)
            return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            
            return item
        else:
            return False
    
    def get_by_category(self,category):
        category_list=[]
        
        for item in self.inventory:
            if item.category==category:
                category_list.append(item)
        
        

        return category_list

    def swap_items(self,friend,item_b,item_d):
        if item_b in self.inventory and item_d in friend.inventory:
            self.inventory.remove(item_b)
            friend.inventory.append(item_b)
            friend.inventory.remove(item_d)
            self.inventory.append(item_d)
        
            return True
        else:
            return False


    def swap_first_item(self,friend):
        if self.inventory != [] and friend.inventory != []:
            my_first_item=self.inventory[0]
            friend_first_item=friend.inventory[0]

            self.inventory.remove(my_first_item)
            friend.inventory.remove(friend_first_item)
            self.inventory.append(friend_first_item)
            friend.inventory.append(my_first_item)
            return True
        else:
            return False

    def get_best_by_category(self,category):
      #how to not do for loop twice?
      i_list=[]
      for object in self.get_by_category(category):
        i_list.append(object.condition)
      for object in self.get_by_category(category):
        if object.condition==max(i_list):
          return object
    
    
    def swap_best_by_category(self,other,my_priority,their_priority):
        if self.inventory != [] and other.inventory != []:

            self.get_best_by_category(their_priority)

            other.get_best_by_category(my_priority)
            self.swap_items(other,self.get_best_by_category(their_priority),other.get_best_by_category(my_priority))  
            return True
        else:
            return False
            
            
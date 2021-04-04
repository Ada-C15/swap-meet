class Vendor: 
    def __init__(self,inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self,item):
    #Not sure if this is the best use of the try and except clause, wanted to attempt as practice. Alternatively, I could have written: 
    #if item not in self.inventory: return False else: self.inventory.remove(item) return item. 
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
    
    def get_by_category(self,category):
        result = []
        for item in self.inventory: 
            if item.category == category: 
                result.append(item)
        return result 


    def swap_items(self,friend_vendor,my_item,their_item): 
        if (my_item in self.inventory and
                their_item in friend_vendor.inventory):
            self.inventory.remove(my_item)
            friend_vendor.inventory.append(my_item)
            friend_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False

    def swap_first_item(self,friend_vendor):
        if len(self.inventory) == 0 or len(friend_vendor.inventory) == 0:
            return False
        
        self.inventory.append(friend_vendor.inventory[0])
        friend_vendor.inventory.append(self.inventory[0])
        self.inventory.remove(self.inventory[0])
        friend_vendor.inventory.remove(friend_vendor.inventory[0])
        return True

    def get_best_by_category(self,category):

        item_in_best_condition_so_far = None
        condition_of_item_in_best_condition_so_far = -1
        for item in self.inventory:
            if item.condition > condition_of_item_in_best_condition_so_far and item.category == category:
                item_in_best_condition_so_far = item
                condition_of_item_in_best_condition_so_far = item.condition
        
        return item_in_best_condition_so_far


    def swap_best_by_category(self,other,my_priority,their_priority): 
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        return self.swap_items(other, my_best, their_best)


    def get_newest(self):
        newest_item_so_far = None
        age_of_newest_item_so_far = None
        for item in self.inventory:
            if newest_item_so_far is None or item.age < age_of_newest_item_so_far:
                newest_item_so_far = item 
                age_of_newest_item_so_far = item.age 

        return newest_item_so_far

    def swap_by_newest(self,other,age=0):
        newest_item_from_self = self.get_newest()
        newest_item_from_other = other.get_newest()
        return self.swap_items(other, newest_item_from_self, newest_item_from_other)

      
        

                

        














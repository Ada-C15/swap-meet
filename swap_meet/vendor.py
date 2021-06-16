from swap_meet.item import Item

#Wave 1 
class Vendor:   
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else: 
            self.inventory = inventory
    
    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

#Wave 2
    def get_by_category(self,category):
        category_list = []

        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list

#Wave 3:
    def swap_items(self,friend, my_item, their_item):
        #if len(self.inventory) == 0 or len(friend.inventory) ==0:
            #return False
        if my_item in self.inventory and their_item in friend.inventory:
            self.inventory.remove(my_item)
            friend.inventory.append(my_item)
            friend.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False

#Wave 4
    def swap_first_item(self,friend):
        if len(self.inventory) == 0 or len(friend.inventory) ==0:
            return False    
        else:
            return self.swap_items(friend,self.inventory[0],friend.inventory[0])            


#Wave 6
    def get_best_by_category(self,category):
        best_item = None
        best_condition = 0
        category_items = self.get_by_category(category)
        if len(category_items) != 0:
            for item in category_items:
                if item.condition > best_condition:
                    best_item = item
                    best_condition = item.condition
        return best_item

    def swap_best_by_category(self,other,my_priority,their_priority):
        their_offer = other.get_best_by_category(my_priority)
        my_offer = self.get_best_by_category(their_priority)
        swap_result = self.swap_items(other,my_offer,their_offer)
        return swap_result   
    

#Wave 7 - Optional Enhancement 
    #Helper function - get item with the min age 
    def get_min_age(self):
        newest_item = None
        min_age = 100

        for item in self.inventory:
              if item.age < min_age:
                newest_item = item
                min_age = item.age
        return newest_item
   
    def swap_by_newest(self,other):
        my_newest = self.get_min_age()
        their_newest = other.get_min_age()
        return self.swap_items(other,my_newest,their_newest)


    
'''    
    #Swap the newest items 
    def swap_by_newest(self,other,my_item,their_item):
        my_newest = self.get_min_age(their_item)
        their_newest = other.get_min_age(my_item)
        return self.swap_items(other,my_newest,their_newest)
        '''

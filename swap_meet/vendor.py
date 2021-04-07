class Vendor():
    def __init__(self, inventory = False):
        self.inventory = list() 
        
        if inventory:
            self.inventory = inventory
      
    
    def add(self, add_item):
        self.inventory.append(add_item)
        return add_item
    
    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else:
            return False
    
    #wave2
    def get_by_category(self, category):
        matching_items = []

        for item in self.inventory:
            if item.category == category:
                matching_items.append(item)
        return matching_items

    #wave3
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory: 
            return False

        self.remove(my_item)
        friend.add(my_item) #add to vendor
        friend.remove(their_item)
        self.add(their_item)
        return True
#wave4
    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False

        my_item = self.inventory[0]
        their_item = friend.inventory[0]
        return self.swap_items(friend, my_item, their_item)

#wave6
    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if len(items) == 0:
            return None
        
        best_by_category = items[0]
        for item in items:
            if item.condition > best_by_category.condition:
                best_by_category = item
        return best_by_category

    def swap_best_by_category(self, other, my_priority, their_priority): 
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        #DRYup using swap_items
        #return self.swap_items(other, my_item, their_item)

        if my_item and their_item:  
            other.remove(their_item)
            self.remove(my_item)
            self.add(their_item)
            other.add(my_item)
            return True
        else:
            return False

        
        




if __name__ == "__main__":
    
    from item import Item
    item1 = Item("jacket")


    x = Vendor()
    print(x.inventory)
    
    y = Vendor([item1])
    print(y.inventory)

    x.add(1)
    print(x.inventory)

    print (x.remove(3))
 
    if x.remove(1):
        print("remove 1")

    y.get_by_category("jacket")
    print(y.get_by_category)
   
        


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
        if my_item not in self.inventory:
            return False
        if their_item not in friend.inventory:
            return False

        self.inventory.remove(my_item)
        friend.inventory.append(my_item)
        
        friend.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True



    def swap_first_item(self, friend):
        
        if len(self.inventory) <= 0:
            return False
        if len(friend.inventory) <= 0:
            return False
        print(self.inventory)
        first_item = self.inventory[0]
        self.inventory.remove(self.inventory[0])
        self.inventory.insert(0, friend.inventory[0])
        print(self.inventory)
            
        friend.inventory.remove(friend.inventory[0])
        friend.inventory.insert(0,first_item)
        return True

    def swap_best_by_category(self, other, my_priority, their_priority):
        if item.category == their_priority:
            return True

    

        



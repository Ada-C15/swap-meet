class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
         
    def get_by_category(self, type_of_stuff):
        matching_items = []
        for item in self.inventory:
            if item.category == type_of_stuff:
                matching_items.append(item)
        return matching_items
        
    def swap_items(self, vendor_friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor_friend.inventory:
            return False
        else:
            self.remove(my_item)
            vendor_friend.add(my_item)
            vendor_friend.remove(their_item)
            self.add(their_item)
            return True
        
            

# defining a method called swap method has 3 arguments
# how to remove an item from inventory 
# it removes the their_item from the vendors invntory and adds it to the friends inventory
# It returns true if all of the above is met
# if vendor inventory doesn't contain my_item or friends inventory doesn't contain their_item       




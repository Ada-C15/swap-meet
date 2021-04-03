
# WAVE 1

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
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False


# WAVE 2

    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
            if item.category == category:
                print(f"The item.category is {item.category}")
                items_list.append(item)
        print(f"The item list is {items_list}")
        return items_list


# WAVE 3
    
    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item) # removes my_item from the main vendor's inventory
            vendor.inventory.append(my_item) # adds my_item to the vendor friend inventory
            vendor.inventory.remove(their_item) # removes their_item from the vendor friend's inventory
            self.inventory.append(their_item) # adds their_item to the main vendor's inventory
            return True
        else:
            return False


# WAVE 4
    
    def swap_first_item(self, vendor):
        if len(self.inventory) != 0 and len(vendor.inventory) != 0:
            vendor.inventory.append(self.inventory[0]) 
            self.inventory.remove(self.inventory[0]) 
            self.inventory.append(vendor.inventory[0]) 
            vendor.inventory.remove(vendor.inventory[0]) 
            return True
        else:
            return False
    

# WAVE 6

    def get_best_by_category(self, category):
        print("HELLO")
        print(len(self.inventory))
        if len(self.inventory) == 0:
            return None
        else:
            # find the item with the highest condition for this category
            items_in_category = self.get_by_category(category)
            print(f"All items in the category {category} are {items_in_category}")
            max_condition = 0
            max_item = None
            for item in items_in_category:
                if item.condition > max_condition:
                    max_condition = item.condition
                    max_item = item
            return max_item
                

            # for i in range(0, len(items_in_category-1)):
            #     if item.condition[i] > item.condition[i+1]:
            #         max = item.condition[i]
            #         i += 1 
            #         print("HI")
            # print(item)
            # return items_in_category[i]
            #   best_item = max(item.condition)
            # return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        # the best item in my inventory with their_priority category is swapped with
        # the best item in other's inventory that matched my_priority category
        # if other has no item matching my_priority category
        return True
        # 

             

      
 








#   for condition in item.condition:
#                     return max(self.condition)
#             best_item = max(items_in_category.condition())
    
    
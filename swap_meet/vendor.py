
class Vendor:
    def __init__ (self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    def add (self, Item):
        self.inventory.append(Item)
        return Item
    def remove(self, Item):
        if Item in self.inventory:
            self.inventory.remove(Item)
            return Item
        else:
            return False

    def get_by_category(self, category):

        found_category_items = []

        for Item in self.inventory:
            if category == Item.category:
                found_category_items.append(Item)
        return found_category_items

    def swap_items(self, Vendor, my_item, their_item):
        if my_item in self.inventory and \
            their_item in Vendor.inventory:
            self.inventory.remove(my_item)
            Vendor.inventory.append(my_item)
            Vendor.inventory.remove(their_item)
            self.inventory.append(their_item)

            return True

        else:

            return False

    def swap_first_item(self, Vendor):

        if self.inventory and Vendor.inventory:

            self.inventory.append(Vendor.inventory[0])
            Vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            Vendor.inventory.remove(Vendor.inventory[0])

            return True

        else:
            
            return False

    def get_best_by_category(self, category):
        
        max_condition = 0
        best_category_Items = []
        winner = None

        for Item in self.inventory:
            if Item.category == category:
                best_category_Items.append(Item)
            
        if best_category_Items == None:
            return None
        
        else:

            for Item in best_category_Items:
                if Item.condition > max_condition:
                    max_condition = Item.condition

            for best_item in best_category_Items:
                if best_item.condition == max_condition:
                    winner = best_item

            return winner
                    
    def swap_best_by_category (self, other, my_priority, their_priority):
        if other.get_best_by_category(my_priority) == None:
            return False
        elif self.get_best_by_category(their_priority) == None:
            return False

        else:
        
            item_i_want = other.get_best_by_category(my_priority)
            item_they_want = self.get_best_by_category(their_priority)

            self.inventory.append(item_i_want)
            other.inventory.append(item_they_want)
            self.inventory.remove(item_they_want)
            other.inventory.remove(item_i_want)

            return True





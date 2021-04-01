
class Vendor:
    def __init__ (self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    def add (self, Item):
        self.inventory.append(Item)
        return item
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
                    

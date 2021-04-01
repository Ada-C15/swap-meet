
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

                

from swap_meet.item import Item

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
    
    def get_by_category(self, category):
    # We have [item_a, item_b, _item_c] as "inventory"
        res = []
        for item in self.inventory: # item_a
            if item.category == category: # if "clothing == clothing": (TRUE)
                res.append(item)

        return res
        


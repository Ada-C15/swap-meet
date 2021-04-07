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
        matched = []
        for item in self.inventory:
            if item.category == category:
                matched.append(item)
        return matched 

    def swap_items(self, them, my_item, their_item):
        if their_item not in them.inventory or my_item not in self.inventory:
            return False 
        else:
            self.inventory.remove(my_item)
            them.inventory.append(my_item)
            them.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True

    def swap_first_item(self, them):
        if len(self.inventory) == 0 or len(them.inventory) == 0:
            return False
        return self.swap_items(them, self.inventory[0], them.inventory[0])

    '''def my_max(items):
            macs = None
            for i in items:
                if macs is None or i.condition > macs.condition:
                    macs = i
            return macs'''

    def get_best_by_category(self, category):
        def get_condition(item):
            return item.condition
        items_in_category = self.get_by_category(category)
        #def my_max would go here if using not using built in max
        if len(items_in_category) > 0: 
            #would have returned my_max(items_in_category) if not using built in max
            return max(items_in_category, key= get_condition)
        else:
            return None
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_category = self.get_best_by_category(their_priority)
        their_category = other.get_best_by_category(my_priority)
        total = self.swap_items(other, my_category, their_category)
        return total
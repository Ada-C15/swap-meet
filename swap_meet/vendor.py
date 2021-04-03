# Swap Meet
# Ada Cohort 15 - Paper
# Katrina Kimzey (she|they)
# Started March 31, 2021

class Vendor:
    def __init__(self, inventory = None):
        # include an inventory
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
        

    def add(self, item):
        # inventory entry
        self.inventory.append(item)
        return item

    def remove(self, item):
        for thing in self.inventory:
            if item == thing:
                self.inventory.remove(thing)
                return thing
        else:
            return False
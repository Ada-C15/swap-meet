class Vendor:
    def __init__(self, inventory=None): #needs to be optional keyword arg
        #inventory is a list
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item): #can this function be called remove?
        if item not in self.inventory:
            return False 
        if item in self.inventory:
           self.inventory.remove(item)#if I use the remove method
           return item
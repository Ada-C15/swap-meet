

# Create a vendor class that has an inventory attribute 
# the inventory attribute can come as a parameter but should not be required 

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
        else:
            return False
        
        return item 


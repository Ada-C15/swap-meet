class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else: 
            self.inventory = inventory 
        
    def adding_to_inventory(Vendor):
        if item in inventory:
            self.inventory.add(item)
        else:
            self.inventory.remove(item)
        return False 
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False 
            
        return item 



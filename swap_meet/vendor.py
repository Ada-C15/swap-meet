class Vendor:
    
    def __init__(self, inventory = None):
        
        #self.inventory = inventory
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    # method, adds item to self.inventory[]
    def add(self,item):
        if item not in self.inventory:
            self.inventory.append(item)
        return item 
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category(self, type_of_stuff):
        categorlist = []
        for item in self.inventory:
            if item.category == type_of_stuff:
                categorlist.append(item)
        return categorlist

                


        


    


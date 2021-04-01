class Vendor: 
    def __init__(self, inventory=None):
        if inventory == None: 
            self.inventory = []
        else: 
            self.inventory = inventory

    def add(self, add_item):
        self.inventory.append(add_item)
        return add_item    
    
    def remove(self, rm_item): 
        if rm_item in self.inventory:
            self.inventory.remove(rm_item)
            return rm_item
        else:
            return rm_item  == False 
    
    def get_by_category(self, asked_category):
        item_list =[]
        for item in self.inventory: 
            if item.category == asked_category:
                item_list.append(item)
        
        return item_list


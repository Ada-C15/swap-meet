from swap_meet.item import Item

class Vendor():

    def __init__(self, inventory = None):

        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
        

    def add(self, item):  
        self.inventory.append(item)
        return item
        

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            for i, element in enumerate(self.inventory):
                if element == item:
                    return self.inventory.pop(i)          
        
    
    def get_by_category(self, category):
        category_list = []
        i = 0
        while len(self.inventory) > i:
            for vendor_item in self.inventory:
                if category == vendor_item.category:
                    category_list.append(vendor_item)
                i+=1               
            return category_list



    





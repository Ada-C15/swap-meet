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
        
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        by_category_list = []
        print("Category:", category)
        for item in category:
            if item.category == "clothing":
                by_category_list.append(item)
        
            
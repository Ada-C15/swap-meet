class Vendor:
    def __init__(self, inventory = None):
    # you can't make an argument/parameter of a mutable data type
    # In python, if the inventory is set to an empty list
    # one instance update ...will change all the instances -
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if self.inventory == []:
            return None
        elif item not in self.inventory:
            return False
        else:
            for remove_item in self.inventory:
                if item == remove_item:
                    self.inventory.remove(remove_item)
                    return remove_item

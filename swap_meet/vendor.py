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
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item


# inventory=[]

# vendor_1 = Vendor(inventory)
# print(vendor_1.inventory)
# print(vendor_1.add("chocolate"))
# print(vendor_1.inventory)

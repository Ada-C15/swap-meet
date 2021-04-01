class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return " ".join(self.inventory)

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        return item
class Vendor():
    def __init__(self, inventory = None):
        if inventory == None:
            inventory = []
        self.inventory = inventory

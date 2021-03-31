class Vendor:

    def __init__(self, inventory=[]):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory 
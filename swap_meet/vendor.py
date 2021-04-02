
class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

# bob = Vendor()
# pam = Vendor()
# bob.inventory.append(["help"])

# print(bob.inventory)
# print(pam.inventory)


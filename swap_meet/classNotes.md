
class Vendor:
    def __init__(self, inventory = None):
        # self.inventory = inventory if you do this bob and jill will end of appending to the same list
        if inventory == None:
            self.inventory = []  # creates new empty list for each instance 
        else:
            self.inventory = inventory 


bob = Vendor()
print(bob.inventory)
print("bobs list", bob.inventory)

jill = Vendor()
jill.inventory.append("bananas")
print("jill list", jill.inventory)

0000"])
print("cheese list", cheese.inventory)

class Vendor:
    def __init__(self, inventory = None):
        # self.inventory = inventory if you do this bob and jill will end of appending to the same list
        if inventory == None:
            self.inventory = []  # creates new empty list for each instance 
        else:
            self.inventory = inventory 

friend = Vendor()
friend.inventory

bob = Vendor()
print(bob.inventory)
print("bobs list", bob.inventory)

jill = Vendor()
jill.inventory.append("bananas")
print("jill list", jill.inventory)

0000"])
print("cheese list", cheese.inventory)

# becca notes on 

class Currency:
    def __init__(self, value, unit="dollar"):
        self.value = value
        self.unit = unit
    
    def converter(self, other_unit):
        pass

    def __lt__(self, other):
        if self.value < other.value:
            return True
        else: 
            return False

    def summary(self):
        return f"{self.value} {self.unit}s"


five = Currency(5)
one = Currency(1)

print(one < five)

print(str(five))
print(five.summary())
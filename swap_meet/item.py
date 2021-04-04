############### TEST WAVE 2 (3 tests) ###############
############### TEST WAVE 5 (5 tests) ###############
# from vendor.swap_meet import Vendor??
# the instances/obects of the Item class will be components of the Vendor class' instance - vendor objects "have many" item objects

### test 2.1 PASSED ### setting the default argument makes it optional
class Item:
    def __init__(self, category = None, condition = None):
        if category == None:
            self.category = ""
        else:
            self.category = category
### test 5.4 PASSED ###
# make sure all conditions are a float
        if condition is None:
            self.condition = float(0)
        else:
            self.condition = float(condition)

### test 3.1 PASSED ### override_to_string / stringify
    def __str__(self):
        return "Hello World!" # use str() to call this method and convert item to the str "Hello World"
# could also return "items category: {self.category}".format(self=self)
# this method turns an item instance into the string "Hello world"

### test 5.5 F ###
    def condition_description(self, condition): 
        condition_description = ""
        if condition < 0 or condition > 5:
            return None
        elif condition <= 1:
            condition_description = "A hot mess"
        elif condition <= 2 and condition > 1:
            condition_description = "some wear and tear, the condition is fair"
        elif condition <= 3 and condition > 2:
            condition_description = "pleantifly medicore"
        elif condition <= 4 and condition > 3:
            condition_description = "pretty darn good"
        elif condition <= 5 and condition > 4:
            condition_description = "supreme"
        return str(condition_description)

# All three classes and the Item class have an instance method
# named condition_description, which should describe the condition in words 
# based on the value, assuming they all range from 0 to 5. These can be basic 
# descriptions (eg. 'mint', 'heavily used') but feel free to have fun with these 
# (e.g. 'You probably want a glove for this one..."). The one requirement is that 
# the condition_description for all three classes above have the same behavior.
############### TEST WAVE 2 (3 tests) ###############
# from vendor.swap_meet import Vendor??
# the instances/obects of the Item class will be components of the Vendor class' instance - vendor objects "have many" item objects

### test 2.1 PASSED ###
class Item:
    def __init__(self, category = None):
        if category == None:
            self.category = ""
        else:
            self.category = category
# setting the default argument to an empty string makes it optional to pass in a string with a keyword argument category

### test 3.1 PASSED ###
# override_to_string / stringify
    def __str__(self):
        return "Hello World!" # use str() to call this method and convert item to the str "Hello World"
    # could also return "items category: {self.category}.format(self=self)

# this function should turn an item instance into the string "Hello world"
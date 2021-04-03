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

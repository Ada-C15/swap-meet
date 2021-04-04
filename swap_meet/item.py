### Wave 2

class Item:
    pass

    def __init__(self, category = ""):
        self.category = category
        return

        

# The first tests in wave 2 imply:

# - There is a module (file) named `item.py` inside of the `swap_meet` package (folder)

# - Inside this module, there is a class named `Item`
# - Each `Item` will have an attribute named `category`, which is an empty string by default
# - When we initialize an instance of `Item`, we can optionally pass in a string with the keyword argument `category`
# - Instances of `Vendor` have an instance method named `get_by_category`
#   - It takes one argument: a string, representing a category
#   - This method returns a list of `Item`s in the inventory with that category

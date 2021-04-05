'''The first tests in wave 2 imply:

- There is a module (file) named `item.py` inside of the `swap_meet` package (folder)

- Inside this module, there is a class named `Item`
- Each `Item` will have an attribute named `category`, which is an empty string by default
- When we initialize an instance of `Item`, we can optionally pass in a string with the keyword argument `category`'''



class Item:
    def __init__(self, category = "", condition=0):
        self.category = category
        self.condition = condition
#wave 3
    def __str__(self):
        return "Hello World!"



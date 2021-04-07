from swap_meet.vendor import Vendor
from swap_meet.item import Item

# shirt = Item(category="clothing")
# phone = Item(category="electronics")
# shoe = Item(category="clothing")
# vendor = Vendor(
#     inventory=[shirt, phone, shoe]
# )
# #print(id(shirt.category))
# print(shoe.category) # should return clothing

# items = vendor.get_by_category("clothing")
# print(items)
# # should return shirt and shoe 

# item_a = Item(category="clothing")
# item_b = Item(category="clothing")
# item_c = Item(category="clothing")
# fatimah = Vendor(
#     inventory=[item_a, item_b, item_c]
# )

# item_d = Item(category="electronics")
# item_e = Item(category="decor")
# jolie = Vendor(
#     inventory=[item_d, item_e]
# )

#result = fatimah.swap_items(jolie, item_a, item_d)

# print(result)
#print(jolie.inventory)
# print(vars(jolie.inventory[0])) # prints out {'category': 'decor'}


### wave 4 ### 

item_a = Item(category="clothing")
item_b = Item(category="clothing")
item_c = Item(category="clothing")
fatimah = Vendor(
    inventory=[item_a, item_b, item_c]
)

item_d = Item(category="electronics")
item_e = Item(category="decor")
jolie = Vendor(
    inventory=[item_d, item_e]
)

result = fatimah.swap_first_item(jolie)
print(result)
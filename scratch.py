from swap_meet.item import Item 
from swap_meet.vendor import Vendor 


item_a = Item(category="clothing")
item_b = Item(category="clothing")
item_c = Item(category="clothing")
fatimah = Vendor(
    inventory=[item_a, item_b, item_c]
)
print(fatimah.inventory)



item_d = Item(category="electronics")
item_e = Item(category="decor")
jolie = Vendor(
    inventory=[item_d, item_e]
)
print("Something at the bottom. ")
result = fatimah.swap_items(jolie, item_b, item_d)
print(result)

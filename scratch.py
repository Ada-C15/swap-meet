from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.electronics import Electronics
# from swap_meet.cllothing import clothing
# from swap_meet.decor import Decor


item_a = Item(category="clothing")
item_b = Item(category="electronics")
item_c = Item(category="clothing")
vendor = Vendor(
    inventory=[item_a, item_b, item_c]
)

items = vendor.get_by_category("clothing")
print(items)

from swap_meet.item import Item 
from swap_meet.vendor import Vendor 
from swap_meet.clothing import Clothing
from swap_meet.electronics import Electronics
from swap_meet.decor import Decor

items = [
        Item(condition = 3.5), Item(condition = 4.0)]
item_a = items[0]
print(item_a.condition)


clothing_item = Clothing(condition = 4.5)
print(clothing_item.condition)





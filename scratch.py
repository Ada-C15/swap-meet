
from swap_meet.item import Item 
from swap_meet.vendor import Vendor 
from swap_meet.clothing import Clothing
from swap_meet.electronics import Electronics
from swap_meet.decor import Decor

items = [
    Clothing(condition=4.8),
    Decor(condition=2.5),
    Electronics(condition=3.2), 
    Clothing(condition=0.8), 
    Decor(condition = 5)
]


for item in items:
    print(item.condition_description())


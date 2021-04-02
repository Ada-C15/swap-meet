from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.electronics import Electronics
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor


tai = Vendor(
    inventory=[]
)

item_a = Clothing(condition=2.0)
item_b = Decor(condition=4.0)
item_c = Clothing(condition=4.0)
jesse = Vendor(
    inventory=[item_a, item_b, item_c]
)

result = tai.swap_best_by_category(
    other=jesse,
    my_priority="Clothing",
    their_priority="Decor"
    )

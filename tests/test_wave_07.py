import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_age():
    item_a = Decor(condition=2.0, age=3)
    item_b = Electronics(condition=4.0, age=2)
    item_c = Decor(condition=4.0, age=1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0, age=2)
    item_e = Decor(condition=4.0, age=1)
    item_f = Clothing(condition=4.0, age=0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(
        other=jesse,
    )

    assert result is True
    assert len(tai.inventory) is 3
    assert len(jesse.inventory) is 3
    assert item_c not in tai.inventory
    assert item_f in tai.inventory
    assert item_f not in jesse.inventory
    assert item_c in jesse.inventory
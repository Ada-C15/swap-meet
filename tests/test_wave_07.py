import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    item_a = Decor(age=2)
    item_b = Electronics(age=7)
    item_c = Clothing(age=0.5)
    johannes = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Electronics(age=10)
    item_e = Decor(age=17)
    item_f = Electronics(age=1)
    leva = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = johannes.swap_by_newest(
        other=leva,
    )

    assert result is True
    assert len(johannes.inventory) is 3
    assert len(leva.inventory) is 3
    assert item_c not in johannes.inventory
    assert item_f in johannes.inventory
    assert item_f not in leva.inventory
    assert item_c in leva.inventory
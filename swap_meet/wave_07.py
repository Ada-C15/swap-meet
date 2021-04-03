import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_swap_by_newest():
    item_a = Decor(age="Vintage")
    item_b = Electronics(age="New")
    item_c = Decor(age="New")
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age="Vintage")
    item_e = Decor(age="New")
    item_f = Clothing(age="New")
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert result is True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_c not in tai.inventory
    assert item_f in tai.inventory
    assert item_f not in jesse.inventory
    assert item_c in jesse.inventory
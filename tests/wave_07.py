import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_swap_by_newest():
    item_a = Decor(age=5.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=1.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=2.0)
    item_e = Decor(age=5.0)
    item_f = Clothing(age=4.0)
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


def test_swap_by_newest_no_match_is_false():
    tai = Vendor(
    inventory=[]
    )

    item_a = Clothing(age=5.0)
    item_b = Decor(age=2.0)
    item_c = Clothing(age=1.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert result is False
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory


def test_swap_by_newest_no_other_match():
    item_a = Clothing(age=5.0)
    item_b = Decor(age=2.0)
    item_c = Clothing(age=1.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert result is False
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory


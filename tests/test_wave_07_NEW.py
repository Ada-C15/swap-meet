import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_get_by_newest():
    item_a = Clothing(age=2)
    item_b = Decor(age=2)
    item_c = Clothing(age=4)
    item_d = Decor(age=5)
    item_e = Clothing(age=1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_by_newest()

    # get_by_newest(self, friend)
    assert newest_item == item_e


def test_swap_by_newest_no_matches_is_none():
    item_a = Decor(age=2.0)
    item_b = Decor(age=1.0)
    item_c = Decor(age=4.0)
    item_d = Decor(age=8.0)

    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    ta = Vendor(
        inventory=[item_d]
    )
    is_swap = tai.swap_by_newest(ta)

    assert is_swap is not False
    assert item_d in tai.inventory
    assert item_b in ta.inventory
    assert item_a not in ta.inventory




def test_swap_by_newest_with_duplicates():
    item_a = Clothing(age=2)
    item_d = Clothing(age=2)
    tai = Vendor(
        inventory=[item_a]
    )
    ta = Vendor(
        inventory=[item_d]
    )
    is_swap = tai.swap_by_newest(ta)

    assert item_a in ta.inventory
    assert is_swap is not False

def test_swap_by_newest_returns_false():
    tai = Vendor(
        inventory=[]
    )

    item_d = Clothing(age=2)
    item_e = Decor()
    item_f = Clothing(age=5)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(
        jesse
    )

    assert result is False

import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_get_newest():
    item_a = Clothing(age=3)
    item_b = Decor(age=5)
    item_c = Clothing(age=4)
    item_d = Decor(age=75)
    item_e = Clothing(age=17)
    sid = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = sid.get_newest()

    assert newest_item.age == 3

def test_get_newest_with_duplicates():
    item_a = Clothing(age=7)
    item_b = Clothing(age=25)
    item_c = Clothing(age=7)
    sid = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item = sid.get_newest()

    assert newest_item.age == 7

def test_get_newest_from_my_empty_returns_false():
    sid = Vendor(
        inventory=[]
    )

    result = sid.get_newest()

    assert len(sid.inventory) is 0
    assert result is None


def test_swap_by_newest():
    item_a = Decor(age=5)
    item_b = Electronics(age=74)
    item_c = Decor(age=10)
    sid = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=24)
    item_e = Decor(age=92)
    item_f = Clothing(age=2)
    ren = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = sid.swap_by_newest(
        other=ren
    )

    assert result is True
    assert len(sid.inventory) is 3
    assert len(ren.inventory) is 3
    assert item_a not in sid.inventory
    assert item_a in ren.inventory
    assert item_f not in ren.inventory
    assert item_f in sid.inventory

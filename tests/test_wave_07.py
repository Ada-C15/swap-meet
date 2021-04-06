import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_items_have_age_as_float():
    items = [
        Clothing(age=15.0),
        Decor(age=15.0),
        Electronics(age=15.0)
    ]
    for item in items:
        assert item.age == pytest.approx(15.0)

def test_get_newest_returns_youngest():
    item_a = Clothing(age=6)
    item_b = Decor(age=2)
    item_c = Clothing(age=1)
    item_d = Decor(age=10)
    item_e = Clothing(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_newest()

    assert newest_item == item_c
    assert newest_item.age == 1


def test_get_newest_with_duplicates():
    item_a = Clothing(age=10)
    item_b = Clothing(age=6)
    item_c = Clothing(age=6)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item = tai.get_newest()

    assert newest_item.age == 6
    assert newest_item == item_b


def test_swap_by_newest():
    item_a = Decor(age=25)
    item_b = Electronics(age=10)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=17)
    item_e = Decor(age=5)
    item_f = Clothing(age=20)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    tai_newest = tai.get_newest()
    jesse_newest = jesse.get_newest()
    result = tai.swap_by_newest(jesse)

    assert result is True
    assert len(tai.inventory) is 3
    assert len(jesse.inventory) is 3
    assert item_c not in tai.inventory
    assert item_e in tai.inventory
    assert item_e not in jesse.inventory
    assert item_c in jesse.inventory

def test_swap_by_newest_no_age_is_false():
    item_d = Electronics()
    tai = Vendor(
        inventory=[item_d]
    )

    item_a = Clothing()
    item_b = Decor()
    item_c = Clothing()
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_by_newest(other=jesse)

    assert result is False
    assert len(tai.inventory) is 1
    assert len(jesse.inventory) is 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory
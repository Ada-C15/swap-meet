import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_get_newest_by_category():
    item_a = Clothing(condition=None, age=2)
    item_b = Decor(condition=None, age=2)
    item_c = Clothing(condition=None, age=4)
    item_d = Decor(condition=None, age=5)
    item_e = Clothing(condition=None, age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = tai.get_newest_by_category("Clothing")

    assert best_item.category == "Clothing"
    assert best_item.age == 4

def test_get_newest_by_category_no_matches_is_none():
    item_a = Decor(age=2)
    item_b = Decor(age=2)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = tai.get_newest_by_category("Electronics")

    assert best_item is None


def test_get_newest_by_category_with_duplicates():
    item_a = Clothing(age=2)
    item_b = Clothing(age=4)
    item_c = Clothing(age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = tai.get_newest_by_category("Clothing")

    assert best_item.category == "Clothing"
    assert best_item.age == 4


def test_swap_by_newest():
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert result is True
    assert len(tai.inventory) is 3
    assert len(jesse.inventory) is 3
    assert item_c not in tai.inventory
    assert item_f in tai.inventory
    assert item_f not in jesse.inventory
    assert item_c in jesse.inventory


def test_swap_by_newest_no_match_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=2)
    item_b = Decor(age=4)
    item_c = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert result is False
    assert len(tai.inventory) is 0
    assert len(jesse.inventory) is 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory


def test_swap_by_newest_no_other_match():
    item_a = Clothing(age=2)
    item_b = Decor(age=4)
    item_c = Clothing(age=4)
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
    assert len(tai.inventory) is 3
    assert len(jesse.inventory) is 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
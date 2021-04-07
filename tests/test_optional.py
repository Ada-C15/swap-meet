import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_newest_by_category():
    item_a = Clothing(age=17)
    item_b = Decor(age=23)
    item_c = Clothing(age=45)
    item_d = Decor(age=56)
    item_e = Clothing(age=37)
    clara = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = clara.get_newest_by_category("Clothing")

    assert best_item.category == "Clothing"
    assert best_item.age == pytest.approx(17)


def test_newest_by_category_no_matches_is_none():
    item_a = Decor(age=67)
    item_b = Decor(age=27)
    item_c = Decor(age=8)
    clara = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = clara.get_newest_by_category("Electronics")

    assert best_item is None


def test_newest_by_category_with_duplicates():
    item_a = Clothing(age=9)
    item_b = Clothing(age=6)
    item_c = Clothing(age=6)
    clara = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = clara.get_newest_by_category("Clothing")

    assert best_item.category == "Clothing"
    assert best_item.age == pytest.approx(6)


def test_swap_newest_by_category():
    item_a = Decor(age=41)
    item_b = Electronics(age=32)
    item_c = Decor(age=28)
    tanae = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=48)
    item_e = Decor(age=17)
    item_f = Clothing(age=23)
    jenda = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tanae.swap_newest_by_category(
        other=jenda,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert result is True
    assert len(tanae.inventory) is 3
    assert len(jenda.inventory) is 3
    assert item_c not in tanae.inventory
    assert item_f in tanae.inventory
    assert item_f not in jenda.inventory
    assert item_c in jenda.inventory


def test_swap_newest_by_category_no_match_is_false():
    tanae = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=17)
    item_b = Decor(age=33)
    item_c = Clothing(age=54)
    jenda = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tanae.swap_newest_by_category(
        other=jenda,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert result is False
    assert len(tanae.inventory) is 0
    assert len(jenda.inventory) is 3
    assert item_a in jenda.inventory
    assert item_b in jenda.inventory
    assert item_c in jenda.inventory


def test_swap_newest_by_category_no_other_match():
    item_a = Clothing(condition=2)
    item_b = Decor(condition=11)
    item_c = Clothing(condition=11)
    tanae = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jenda = Vendor(
        inventory=[]
    )

    result = tanae.swap_newest_by_category(
        other=jenda,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert result is False
    assert len(tanae.inventory) is 3
    assert len(jenda.inventory) is 0
    assert item_a in tanae.inventory
    assert item_b in tanae.inventory
    assert item_c in tanae.inventory



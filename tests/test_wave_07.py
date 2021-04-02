import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_best_by_edge():
    item_a = Electronics(edge=1.0)
    item_b = Decor(edge=2.0)
    item_c = Electronics(edge=4.0)
    item_d = Decor(edge=5.0)
    item_e = Electronics(edge=3.0)
    mary = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = mary.get_best_by_edge("Electronics")

    assert newest_item.category == "Electronics"
    assert newest_item.edge == pytest.approx(1.0)

def test_best_by_edge_no_matches_is_none():
    item_a = Electronics(edge=1.0)
    item_b = Decor(edge=2.0)
    item_c = Electronics(edge=4.0)
    item_d = Decor(edge=5.0)
    item_e = Electronics(edge=3.0)
    mary = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = mary.get_best_by_edge("Clothing")

    assert newest_item is None


def test_best_by_edge_with_duplicates():
    item_a = Clothing(edge=2.0)
    item_b = Clothing(edge=2.0)
    item_c = Clothing(edge=4.0)
    mary = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item = mary.get_best_by_edge("Clothing")

    assert newest_item.category == "Clothing"
    assert newest_item.edge == pytest.approx(2.0)


def test_swap_by_edge():
    item_a = Decor(edge=2.0)
    item_b = Electronics(edge=4.0)
    item_c = Decor(edge=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(edge=2.0)
    item_e = Decor(edge=4.0)
    item_f = Clothing(edge=4.0)
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
    assert item_a not in tai.inventory
    assert item_d in tai.inventory
    assert item_d not in jesse.inventory
    assert item_a in jesse.inventory


def test_swap_by_edge_no_match_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(edge=2.0)
    item_b = Decor(edge=3.0)
    item_c = Clothing(edge=3.0)
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


def test_swap_by_edge_no_other_match():
    item_a = Clothing(edge=2.0)
    item_b = Decor(edge=4.0)
    item_c = Clothing(edge=4.0)
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




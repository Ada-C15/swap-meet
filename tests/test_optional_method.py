import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_get_newest_item():
    item_a = Clothing(year=2005)
    item_b = Electronics(year=2002)
    item_c = Clothing(year=1955)
    item_d = Decor(year=1982)
    item_e = Clothing(year=2013)
    madison = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = madison.get_newest_item()
    
    assert newest_item.year == 2013
    assert newest_item.age == 8
    assert newest_item.category == "Clothing"


def test_get_newest_item_empty_inventory_is_none():
    madison = Vendor(
        inventory=[]
    )
    newest_item = madison.get_newest_item()

    assert newest_item is None


def test_newest_item_with_duplicates():
    item_a = Decor(year=1999)
    item_b = Electronics(year=1970)
    item_c = Clothing(year=1999)
    madison = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    newest_item = madison.get_newest_item()

    assert newest_item.age == 22
    assert newest_item.year == 1999

def test_swap_by_newest():
    item_a = Decor(year=2001)
    item_b = Electronics(year=1937)
    item_c = Decor(year=2016)
    madison = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(year=2018)
    item_e = Decor(year=1995)
    item_f = Clothing(year=2019)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = madison.swap_by_newest(
        other_vendor=jesse,
    )

    assert result is True
    assert len(madison.inventory) is 3
    assert len(jesse.inventory) is 3
    assert item_c not in madison.inventory
    assert item_f in madison.inventory
    assert item_f not in jesse.inventory
    assert item_c in jesse.inventory


def test_swap_by_newest_empty_inventory_returns_False():
    madison = Vendor(
        inventory=[]
    )

    item_d = Clothing(year=2018)
    item_e = Decor(year=1995)
    item_f = Clothing(year=2019)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = madison.swap_by_newest(
        other_vendor=jesse,
    )

    assert result is False
    assert len(madison.inventory) is 0
    assert len(jesse.inventory) is 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

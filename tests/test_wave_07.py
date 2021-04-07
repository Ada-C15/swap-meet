import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.electronics import Electronics

def test_get_newest_item():
    item_a = Item(age = 3)
    item_b = Item(age = 1)
    item_c = Item(age = 2)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    newest_item = fatimah.get_newest_item()

    assert newest_item.age == pytest.approx(1.0)


def test_get_newest_item_with_duplicates():
    item_a = Item(age = 3)
    item_b = Item(age = 1)
    item_c = Item(age = 1)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    newest_item = fatimah.get_newest_item()

    assert newest_item.age == pytest.approx(1.0)

def test_swap_by_newest():
    item_a = Item(age = 3)
    item_b = Item(age = 1)
    item_c = Item(age = 2)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age = 4)
    item_e = Item(age = 5)
    item_f = Item(age = 2)
    jolie = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = fatimah.swap_by_newest(
        business_partner = jolie, 
        my_newest_item = item_b, 
        their_newest_item = item_f)

    assert result is True
    assert len(fatimah.inventory) is 3
    assert len(jolie.inventory) is 3
    assert item_b not in fatimah.inventory
    assert item_f in fatimah.inventory
    assert item_f not in jolie.inventory
    assert item_b in jolie.inventory
    
def test_swap_by_newest_from_my_empty_returns_false():
    fatimah = Vendor(
        inventory=[]
    )

    item_d = Item(age = 4)
    item_e = Item(age = 5)
    item_f = Item(age = 2)
    jolie = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    nobodys_item = Item(age = 3)

    result = fatimah.swap_by_newest(jolie, nobodys_item, item_f)

    assert len(fatimah.inventory) is 0
    assert len(jolie.inventory) is 3
    assert result is False

def test_swap_by_newest_from_their_empty_returns_false():
    item_a = Item(age = 3)
    item_b = Item(age = 1)
    item_c = Item(age = 2)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jolie = Vendor(
        inventory=[]
    )

    nobodys_item = Item(age = 3)

    result = fatimah.swap_by_newest(jolie, item_b, nobodys_item)

    assert len(fatimah.inventory) is 3
    assert len(jolie.inventory) is 0
    assert result is False
import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_items_have_age_as_int():
    items = [
        Clothing(age=3),
        Decor(age=3),
        Electronics(age=3)
    ]
    for item in items:
        assert item.age == pytest.approx(3)



def test_get_newest():
    item_a = Clothing(age=2)
    item_b = Decor(age=2)
    item_c = Clothing(age=4)
    item_d = Decor(age=5)
    item_e = Clothing(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_newest("Clothing")

    assert newest_item.category == "Clothing"
    assert newest_item.age == pytest.approx(2)



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
        my_newest="Decor",
        their_newest="Clothing"
    )

    assert result is True
    assert len(tai.inventory) is 3
    assert len(jesse.inventory) is 3
    assert item_a not in tai.inventory
    assert item_d in tai.inventory
    assert item_d not in jesse.inventory
    assert item_a in jesse.inventory
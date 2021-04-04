import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    item_a = Decor(age=2)
    item_b = Electronics(age=7)
    item_c = Clothing(age=0.5)
    johannes = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Electronics(age=10)
    item_e = Decor(age=17)
    item_f = Electronics(age=1)
    live = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = johannes.swap_by_newest(
        other=live
    )

    assert result is True
    assert len(johannes.inventory) is 3
    assert len(live.inventory) is 3
    assert item_c not in johannes.inventory
    assert item_f in johannes.inventory
    assert item_f not in live.inventory
    assert item_c in live.inventory    


def test_swap_by_newest_works_with_really_old_items():
    item_a = Clothing(age=3857327832)
    item_b = Decor(age=3758239357346849)
    item_c = Electronics(age=73728834859649327)
    johannes = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Electronics(age=863993285383268)
    item_e = Decor(age=869393864386548438)
    item_f = Clothing(age=94639489)
    live = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = johannes.swap_by_newest(
        other = live
    )

    assert result is True
    assert len(johannes.inventory) is 3
    assert len(live.inventory) is 3
    assert item_a not in johannes.inventory
    assert item_f in johannes.inventory
    assert item_f not in live.inventory
    assert item_a in live.inventory

def test_swap_by_newest_returns_false_with_empty_inventory():
    johannes = Vendor()
    
    live = Vendor()

    result = johannes.swap_by_newest(
        other=live
    )

    assert result is False


def test_swap_by_newest_swaps_first_item_when_all_items_are_same_age():
    item_a = Clothing(age=5)
    item_b = Decor(age=5)
    item_c = Electronics(age=5)
    johannes = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Electronics(age=5)
    item_e = Decor(age=5)
    item_f = Clothing(age=5)
    live = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = johannes.swap_by_newest(
        other = live
    )

    assert result is True
    assert len(johannes.inventory) is 3
    assert len(live.inventory) is 3
    assert item_a not in johannes.inventory
    assert item_d in johannes.inventory
    assert item_d not in live.inventory
    assert item_a in live.inventory
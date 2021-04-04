import pytest
from swap_meet.clothing import Clothing
from swap_meet.electronics import Electronics
from swap_meet.decor import Decor
from swap_meet.vendor import Vendor
from swap_meet.item import Item

def test_get_min_age():
    item_a = Decor(condition=3.5)
    item_b = Electronics(condition=3.5)
    item_c = Clothing(condition=3.5, age=9.0)
    item_d = Item(condition=3.5, age=1.0)
    item_e = Clothing(condition=3.5, age=6.0)

    kate = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    result = kate.get_min_age()

    assert result.category == "Electronics"
    assert result.age == pytest.approx(0.0)

def test_get_min_age_return_none():
    jenny = Vendor(
        inventory=[]
    )

    result = jenny.get_min_age()

    assert result == None

def test_swap_by_newest_return_true():
    item_a = Electronics(condition=3.5, age=7.0)
    item_b = Item(condition=3.5, age=5.0)
    item_c = Decor(condition=3.5, age=2.0)

    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
        )
        
    item_d = Item(condition=3.5, age=7.0)
    item_e = Decor(condition=3.5, age=3.0)
    item_f = Clothing(condition=3.5, age=9.0)

    mai = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = jesse.swap_by_newest(mai)

    assert result is True
    assert len(mai.inventory) is 3
    assert len(jesse.inventory) is 3
    assert item_c not in jesse.inventory
    assert item_a in jesse.inventory
    assert item_e not in mai.inventory
    assert item_f in mai.inventory

def test_swap_by_newest_my_list_is_empty_return_false():
    patrick = Vendor(inventory=[])
        
    item_a = Decor(condition=3.5, age=7.0)
    item_b = Electronics(condition=3.5, age=3.0)
    item_c = Clothing(condition=3.5, age=9.0)

    katrina = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = patrick.swap_by_newest(katrina)

    assert result is False
    assert len(patrick.inventory) is 0
    assert len(katrina.inventory) is 3

def test_swap_by_newest_their_list_is_empty_false():
    item_a = Decor(condition=3.5, age=7.0)
    item_b = Electronics(condition=3.5, age=3.0)
    item_c = Clothing(condition=3.5, age=9.0)

    peter = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    tom = Vendor(inventory=[])
    
    result = peter.swap_by_newest(tom)

    assert result is False
    assert len(tom.inventory) is 0
    assert len(peter.inventory) is 3

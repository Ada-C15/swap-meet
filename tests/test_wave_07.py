import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_get_min_age():
    item_a = Clothing(age = 1)
    item_b = Clothing(age = 4)
    item_c = Decor(age = 2)
    item_d = Decor(age = 3.5)
    tai = Vendor(inventory = [item_a,item_b,item_c, item_d])
    newest_item = tai.get_min_age()
    
    assert newest_item.age == 1

def test_swap_by_newest():
    item_a = Item(age=2)
    item_b = Item(age=4)
    tai = Vendor(inventory=[item_a, item_b]) 

    item_d = Item(age=2)
    item_e = Item(age=4)
    jesse = Vendor(inventory=[item_d, item_e])   
    result = tai.swap_by_newest(jesse)

    assert result is True


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



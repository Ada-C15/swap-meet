from swap_meet.vendor import Vendor
from swap_meet.item import Item

def test_swap_by_newest_return_ture():
    item_a = Item(condition=3.5, age=7)
    item_b = Item(condition=3.5, age=5)
    item_c = Item(condition=3.5, age=2)

    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
        )
        
    item_d = Item(condition=3.5, age=7)
    item_e = Item(condition=3.5, age=3)
    item_f = Item(condition=3.5, age=9)

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

def test_swap_by_newest_return_false():
    patrick = Vendor(inventory=[])
        
    item_a = Item(condition=3.5, age=7)
    item_b = Item(condition=3.5, age=3)
    item_c = Item(condition=3.5, age=9)

    katrina = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = patrick.swap_by_newest(katrina)

    assert result is False
    assert len(patrick.inventory) is 0
    assert len(katrina.inventory) is 3


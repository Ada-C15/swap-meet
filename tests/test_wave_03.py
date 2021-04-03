import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

# TEST 9 - PASSED
# @pytest.mark.skip(reason="no way of currently testing this")
def test_item_overrides_to_string():
    # arrange
    item = Item() # item = "" 
    # act
    stringified_item = str(item) 
    # assert
    assert stringified_item == "Hello World!"

# TEST 10 - PASSED
# @pytest.mark.skip(reason="no way of currently testing this")
def test_swap_items_returns_true():
    # arrange
    item_a = Item(category="clothing")
    item_b = Item(category="clothing")
    item_c = Item(category="clothing")
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(category="electronics")
    item_e = Item(category="decor")
    jolie = Vendor(
        inventory=[item_d, item_e]
    )
    # fatima.swap_items(jolie, ...,...)
    # act
    result = fatimah.swap_items(jolie, item_b, item_d)

    # assert
    assert len(fatimah.inventory) is 3
    assert item_b not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_d in fatimah.inventory
    assert len(jolie.inventory) is 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory
    assert item_b in jolie.inventory
    assert result is True

# TEST 11 - PASSED
# @pytest.mark.skip(reason="no way of currently testing this")
def test_swap_items_when_my_item_is_missing_returns_false():
    # arrange
    item_a = Item(category="clothing")
    item_b = Item(category="clothing")
    item_c = Item(category="clothing")
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(category="electronics")
    item_e = Item(category="decor")
    jolie = Vendor(
        inventory=[item_d, item_e]
    )
    # act
    result = fatimah.swap_items(jolie, item_e, item_d)
    # assert
    assert len(fatimah.inventory) is 3
    assert item_d not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert len(jolie.inventory) is 2
    assert item_d in jolie.inventory
    assert item_e in jolie.inventory
    assert result is False

# TEST 12 - PASSED
# @pytest.mark.skip(reason="no way of currently testing this")
def test_swap_items_when_their_item_is_missing_returns_false():
    # arrange
    item_a = Item(category="clothing")
    item_b = Item(category="clothing")
    item_c = Item(category="clothing")
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(category="electronics")
    item_e = Item(category="decor")
    jolie = Vendor(
        inventory=[item_d, item_e]
    )
    # act
    result = fatimah.swap_items(jolie, item_b, item_c)

    # assert
    assert len(fatimah.inventory) is 3
    assert item_d not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert len(jolie.inventory) is 2
    assert item_d in jolie.inventory
    assert item_e in jolie.inventory
    assert result is False

# TEST 13 - PASSED
# @pytest.mark.skip(reason="no way of currently testing this")
def test_swap_items_from_my_empty_returns_false():
    # arrange
    fatimah = Vendor(
        inventory=[]
    )

    item_d = Item(category="electronics")
    item_e = Item(category="decor")
    jolie = Vendor(
        inventory=[item_d, item_e]
    )
    # act
    nobodys_item = Item(category="clothing")

    result = fatimah.swap_items(jolie, nobodys_item, item_d)

    # assert
    assert len(fatimah.inventory) is 0
    assert len(jolie.inventory) is 2
    assert result is False

# TEST 14 - PASSED
# @pytest.mark.skip(reason="no way of currently testing this")
def test_swap_items_from_their_empty_returns_false():
    # arrange
    item_a = Item(category="clothing")
    item_b = Item(category="clothing")
    item_c = Item(category="clothing")
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jolie = Vendor(
        inventory=[]
    )
    # act
    nobodys_item = Item(category="clothing")

    result = fatimah.swap_items(jolie, item_b, nobodys_item)
    # assert
    assert len(fatimah.inventory) is 3
    assert len(jolie.inventory) is 0
    assert result is False
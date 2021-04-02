import pytest
# The following line imports the Vendor class from the module vendor inside the swap_meet package.
from swap_meet.vendor import Vendor

# TEST 1 = PASSED
# @pytest.mark.skip(reason="no way of currently testing this")
def test_vendor_has_inventory(): # has
    # arrange, act - 
    vendor = Vendor()
    #assert
    assert len(vendor.inventory) is 0

# TEST 2 - PASSED
# @pytest.mark.skip(reason="no way of currently testing this")
def test_vendor_takes_optional_inventory(): # takes
    # arrange
    inventory = ["a", "b", "c"]
    # act
    vendor = Vendor(inventory=inventory)
    #assert
    assert len(vendor.inventory) is 3
    assert "a" in inventory
    assert "b" in inventory
    assert "c" in inventory

# TEST 3 - PASSED
# @pytest.mark.skip(reason="no way of currently testing this")
def test_adding_to_inventory():
    #arrange
    vendor = Vendor()
    item = "new item"
    #act
    result = vendor.add(item)
    #assert
    assert len(vendor.inventory) is 1
    assert item in vendor.inventory
    assert result is item

# TEST 4
# @pytest.mark.skip(reason="no way of currently testing this")
def test_removing_from_inventory_returns_item():
    # arrange
    item = "item to remove"
    vendor = Vendor(
        inventory=["a", "b", "c", item]
    )
    # act
    result = vendor.remove(item)
    # assert
    assert len(vendor.inventory) is 3
    assert item not in vendor.inventory
    assert result is item

# TEST 5
# @pytest.mark.skip(reason="no way of currently testing this")
def test_removing_not_found_is_false():
    # arrange
    item = "item to remove"
    vendor = Vendor(
        inventory=["a", "b", "c"]
    )
    # act
    result = vendor.remove(item)
    # assert
    assert len(vendor.inventory) is 3
    assert result is False

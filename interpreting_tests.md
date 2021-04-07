# Wave 1

- [X] Need a vendor.py module (file) in the swap_meet package (folder)

### def test_vendor_has_inventory():
- [X] vendor.py needs a class Vendor()
- [X] Vendor() has an attribute inventory which is an empty list, and it takes an argument inventory

### def test_vendor_takes_optional_inventory():
- [X] Vendor() CAN take a list as an argument and then updates its inventory attribute with the contents of that list, but doesn't have to; if it does take a list, the elements of each list should be added to inventory one by one

### def test_adding_to_inventory():
- [X] Vendor() CAN also take a single element and add that to its inventory list attribute too
- [X] Vendor() has an instance method add() 
    - [X] takes one param (item)
    - [X] adds item to vendor.inventory attribute 
    - [X] returns the item that was added

### def test_removing_from_inventory_returns_item():
- [X] Vendor has an instance method remove()  
    - [X] takes one param (item)
    - [X] removes item from vendor.inventory attribute
    - [X] returns the item that was removed 

### def test_removing_not_found_is_false():
- [X] if remove() is attempted on an items that's not in vendor.inventory, remove() returns False 

==============================================================================

# Wave 2

### def test_items_have_blank_default_category():
- [X] There is an Item class in an item module, which has a 'category' attribute that is initialized as an empty string

### def test_get_items_by_category():
- [X] Vendor has an instance method get_by_category(category) with 1 parameter (category) 
- [X] this instance method checks the Vendor's inventory attribute, which contains a list of Item instances, for Item instances with a category attribute that matches the category argument passed into get_by_category()
- [X] if they match, get_by_category() returns a list of the items witht he matching category attribte 
- [X] notice that this test just wants the method to review a view item for each object, not the a list with names of items -- i.e. the method should return something like [<swap_meet.item.Item object at 0x105f41fa0>, <swap_meet.item.Item object at 0x105f41f40>] 

### def test_get_no_matching_items_by_category():
- [X] get_by_category() method should return an empty list if it can't find any items with the passed-in category attribute

==============================================================================

# Wave 3

### def test_item_overrides_to_string():
- [X] implies `Item` overrides its stringify method (?) and returns "Hello World!" when `str()` is called on an instance of `Item` 

### def test_swap_items_returns_true():
- [X] Create an instance method `swap_items()` for `Vendor` that, given two instances of `Vendor` both with an `inventory` attribute of items:
    - [X] takes three arguments: `friend, my_item, their_item`
    - [X] takes the `my_item` item out of the Vendor (the recipient, whom the method is being called on) instance's inventory  
    - [X] adds the `their_item` item from the inventory of the `friend` (instance of Vendor) and adds it to the receipent Vendor instance's `inventory` 
    - [X] returns True

### def test_swap_items_when_my_item_is_missing_returns_false():
- [ ] `swap_items()` should return False if `my_item` is not in the main Vendor's `inventory` attribute 

### def test_swap_items_when_their_item_is_missing_returns_false():
- [ ] `swap_items()` should return False if `their_item` is not in the `friend` Vendor's `inventory` attribute 

### def test_swap_items_from_my_empty_returns_false():
- [ ] `swap_items()` should return False if `inventory` of recipient Vendor is empty (falsey)

### def test_swap_items_from_their_empty_returns_false():
- [ ] `swap_items()` should return False if `inventory` of `friend` is empty (falsey)

==============================================================================

# Wave 4

### def test_swap_first_item_returns_true():
- [X] `Vendor()` has an instance method `swap_first_item` which
    - [X] takes one parameter, `friend` 
    - [X] removes first item in `inventory` of `friend` and adds to `inventory` of recipient Vendor
    - [X] removes first item in `inventory` of recipient Vendor and adds to `inventory` of `friend`
    - [X] returns True

### def test_swap_first_item_from_my_empty_returns_false():
- [X] `swap_first_item` returns False if recipient Vendor has no inventory 

### def test_swap_first_item_from_their_empty_returns_false():
- [X] `swap_first_item` returns False if `friend` has no inventory 

==============================================================================

# Wave 5

### def test_clothing_has_default_category_and_to_str():

### def test_decor_has_default_category_and_to_str():

### def test_electronics_has_default_category_and_to_str():

### def test_items_have_condition_as_float():
- [X] The `Clothing, Decor, Electronics, Item` classes have an attribute `condition` which stores a float value
- [X] `condition` has to be initialized as a float value

### def test_items_have_condition_descriptions_that_are_the_same_regardless_of_type():
- [ ] The `Clothing, Decor, Electronics, Item` classes have an instance method `condition_description`

==============================================================================

# Wave 6

### def test_best_by_category():
- [X] `Vendor` should have an instance method `get_best_by_category()` 
    - [X] takes `category` as an argument 
    - [X] loops over each `item` instance inside the `inventory` list attribute of `Vendor` 
    - [x] if the '`category` attribute of `item` matches the argument passed into `get_best_by_category()`, the method returns the `item` with the highest `condition` (attribute of `item`) value 

### def test_best_by_category_no_matches_is_none():
- [X] `get_best_by_category()` returns `None` if method finds no items with matching `category` attribute

### def test_best_by_category_with_duplicates():
- [X] this test should pass if that `get_best_by_category()`  was written correctly to begin with

### def test_swap_best_by_category():
- [X] `Vendor` has an instance method `swap_best_by_category()`
    - [X] takes 3 arguments: `other, my_priority, their_priority`
    - [ ] compare each item in `inventory` attribute between self and `other`
        - [ ] keep swapping items until no items with `my_priority` category remain in `other.inventory` and vice versa 
    - [ ] returns `True` 

### def test_swap_best_by_category_no_match_is_false():

### def test_swap_best_by_category_no_other_match():

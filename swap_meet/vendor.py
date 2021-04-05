class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory


    def add(self, item):
        self.inventory.append(item)
        return item


    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False


    def get_by_category(self, category):
        category_items = []
        for specific_item in self.inventory:
            if specific_item.category == category:
                category_items.append(specific_item)

        return category_items


    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        self.add(their_item)

        return True


    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
        return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])


    def get_best_by_category(self, category):
        items_list = []
        best_condition = 0
        for match in self.inventory:
            if match.category == category:
                items_list.append(match)
        if not items_list:
            return None
        for item in items_list:
            if item.condition > best_condition:
                best_condition = item.condition
                goodie = item

        return goodie

    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if their_best_item == None or my_best_item == None:
            return False
        return self.swap_items(other, my_best_item, their_best_item)


    #...Optional Enhancement...
    def get_newest_by_category(self, category):
    ''' --- Explanation ---
    This method returns a newest item in given category
	- get the newest item in a certain category
    - make a list that matches to matching category
    - if list is not empty - we have matching category 
    - loop through the list and check the newest item'''
        newest_items = []
        old_item = 100
        newest_item = 0
        for lifespan in self.inventory:
            if lifespan.category == category:
                newest_items.append(lifespan)
        if not newest_items:
            return None
        for item in newest_items:
            if item.age < old_item:
                old_item = item.age
                newest_item = item

        return newest_item

    def swap_by_newest(self, other, my_newest, their_newest):
        my_newest = self.get_newest_by_category(their_newest)
        their_newest = other.get_newest_by_category(my_newest)

        return self.swap_items(other, my_newest, their_newest)






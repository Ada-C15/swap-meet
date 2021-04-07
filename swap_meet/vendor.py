from swap_meet.item import Item

class Vendor():
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category_string):
        list_of_items_based_on_category = []
        for items in self.inventory:
            if items.category == category_string:
                list_of_items_based_on_category.append(items)
        return list_of_items_based_on_category

    def swap_items(self, friends_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in friends_vendor.inventory:
                self.add(their_item)
                self.remove(my_item)
                friends_vendor.add(my_item)
                friends_vendor.remove(their_item)
                return True
        return False
        
    def swap_first_item(self,friends_vendor):
        if len(self.inventory) == 0 or len(friends_vendor.inventory) == 0:
            return False 
        else:
            friends_vendor.add(self.inventory[0])
            self.remove(self.inventory[0])
            self.add(friends_vendor.inventory[0])
            friends_vendor.remove(friends_vendor.inventory[0])
            return True

    def get_best_by_category(self, best_category):
        list_by_category = self.get_by_category(best_category)
        if len(list_by_category) == 0:
            return None

        elif len(list_by_category) > 0:
            best_item = list_by_category[0]
            for items in list_by_category:
                if best_item.condition < items.condition:
                    best_item = items
            return best_item
    def swap_best_by_category(self, other, my_priority, their_priority):
        their_category = other.get_best_by_category(my_priority)
        my_category = self.get_best_by_category(their_priority)
        return self.swap_items(other, my_category, their_category)
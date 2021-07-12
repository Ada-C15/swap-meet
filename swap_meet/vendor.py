class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory or []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        # for to check if in there
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]
        # # Equivalent to
        # output = []
        # for item in self.inventory:
        #     if item.category == category:
        #         output.append(item)
        # return output

    def swap_items(self, other, my_item, their_item):
        if my_item in self.inventory and their_item in other.inventory:
            self.remove(my_item)
            other.add(my_item)

            other.remove(their_item)
            self.add(their_item)

            return True
        else:
            return False

    def swap_first_item(self, other):
        if self.inventory and other.inventory:
            return self.swap_items(other, self.inventory[0], other.inventory[0])
        else:
            return False

    def get_best_by_category(self, category):
        # # without lambda
        # def get_condition(item):
        #     return item.condition
        # return max(self.get_by_category(category), default=None, key=get_condition)

        # lambda item: item.condition is equivalent to JS: item => item.condition
        return max(self.get_by_category(category), default=None, key=lambda item: item.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        return self.swap_items(
            other, 
            my_item=self.get_best_by_category(their_priority),
            their_item=other.get_best_by_category(my_priority))

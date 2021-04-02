from .item import Item
import operator

class Vendor:


    def __init__(self, inventory = None):
        '''constructs instance of Vendor, 
        initializing inventory with default None'''
        
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        '''receives item as an argument and adds it to Vendor inventory'''
        
        self.inventory.append(item)
        return item

    def remove(self, item):
        '''receives item as an argument and removes it from Vendor inventory'''
        
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        return item
    
    def get_by_category(self, category):
        '''receives category as an argument,
        creates and returns a list of items in that category'''

        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, other_vendor, item_a, item_b):
        '''receives other vendor and items as arguments,
        exchanges those items using add and remove methods'''

        if item_a in self.inventory and item_b in other_vendor.inventory:
            other_vendor.add(item_a)
            self.remove(item_a)
            other_vendor.remove(item_b)
            self.add(item_b)
            return True
        else:
            return False
        
    def swap_first_item(self, other_vendor):
        '''exchanges first item in self.inventory with first item in other_vendor.inventory'''

        if self.inventory and other_vendor.inventory:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
        else:
            return False
    
    def get_best_by_category(self, category):
        '''first calls get_by_category module with category as an argument,
            sorts items low to high by condition using operator.attrgetter,
            returns last/highest item in the sorted list'''

        items = self.get_by_category(category)
        if not items:
            return None
        sorted_items = sorted(items, key=operator.attrgetter('condition'))
        return sorted_items[-1]
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''swaps best items from two vendors,
        employs get_best_by_category, using opposing priorities as an argument'''

        vendor_best = self.get_best_by_category(their_priority)
        other_vendor_best = other.get_best_by_category(my_priority)
        return self.swap_items(other, vendor_best, other_vendor_best)




            
            
                
        
        


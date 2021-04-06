# class Vendor:
#     def __init__(self, inventory_list):
#         self.inventory_list = inventory_list
    
#     def __repr__(self):
#         return self.inventory_list
    
#     def print_it(self):
#         vendor_prime = Vendor(self.inventory_list)
#         print('seller wares are: ', vendor_prime)

#     def get_best_by_category(self, category):
#             contenders = []
#             for item in self.inventory:
#                 if item.category == category:
#                     contenders.append(item)
#                 elif category not in self.inventory:
#                     return None

#             highest_rated_item = max(contenders)
#             return highest_rated_item

# im_vendor = Vendor(['socks', 'gameboy', 'book'])
# print(im_vendor.__repr__())
# im_vendor.get_best_by_category(category="Clothing")
lista = ['cloth', 'cloth', 'cloth', 'app', 'toy']

# for item in lista:
#     control_val = item['cloth']
#     if control_val == False and control_val not in lista:
#         print(control_val, ' is not in this list')
#     elif control_val in lista:
#         print('Here it is: ', control_val)
seta = (set(lista))
print(type(seta))
print(seta)
print(max(seta))
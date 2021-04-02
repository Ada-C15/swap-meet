class Item:
    def __init__(self, category = "", condition = 0):
        '''constructs instance of Item with default condition of 0'''

        self.category = category
        self.condition = float(condition)
    
    def __str__(self):
        '''prints message for the class'''
        return "Hello World!"
    
    def condition_description(self):
        '''prints condition of the instance of the Item'''
        
        return f"The condition of this item is rated as a {self.condition}"


    


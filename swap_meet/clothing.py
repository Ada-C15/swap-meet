from .item import Item
class Clothing(Item):
    def __init__(self, condition = 0):
        '''constructs an instance of Clothing,
        which is an instance of Item,
        with a default condition of 0'''

        super().__init__("Clothing", condition)
       
    
    def __str__(self):
        '''prints message for class'''

        return "The finest clothing you could wear."

    def condition_description(self):
        '''prints instance condition,
        employing condition_description from parent class (Item)'''

        return super().condition_description()
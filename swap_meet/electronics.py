from .item import Item
class Electronics(Item):
    def __init__(self, condition =0):
        '''constructs an instance of Electronics,
        which is an instance of Item,
        with a default condition of 0'''

        super().__init__("Electronics", condition)
       
    
    def __str__(self):
        '''prints message for class'''

        return "A gadget full of buttons and secrets."
    
    def condition_description(self):
        '''prints instance condition,
        employing condition_description from parent class (Item)'''

        return super().condition_description()
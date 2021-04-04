from swap_meet.item import Item

#wave_5
class Electronics(Item):
    """
    inheritance code from method condittion_description 
    """
    def __init__(self, category = "Electronics", condition = 0):
        self.category = "Electronics"
        self.condition = condition 

        super().__init__("Electronics", condition)
    
    def __str__(self):
        return ("A gadget full of buttons and secrets.")
    
    def condition_description(self):
        return super().condition_description()




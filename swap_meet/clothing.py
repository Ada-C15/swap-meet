from swap_meet.item import Item

#wave_5
class Clothing(Item):
    """
    inheritance code from method condittion_description 

    """
    def __init__(self, category = "Clothing", condition = 0):
        self.category = "Clothing"
        self.condition = condition 

        super().__init__("Clothing", condition)
    
    def __str__(self):
        return ("The finest clothing you could wear.")
    
    def condition_description(self):
        return super().condition_description()
        

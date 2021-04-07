from swap_meet.item import Item

#wave_5
class Decor(Item):
    """
    inheritance code from method condittion_description 
    """
    def __init__(self, category = "Decor", condition = 0):
        self.category = "Decor"
        self.condition = condition
        
        super().__init__("Decor", condition)
    
    def __str__(self):
        return ("Something to decorate your space.")

    def condition_description(self):
        return super().condition_description()
        
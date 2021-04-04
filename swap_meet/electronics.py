from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition=None):
        self.category = "Electronics"
        if condition == None:
            self.condition = 0
        else:
            self.condition = float(condition)

    """
    This function utilizes inheritance and takes the 
    functionality from the condition.description method
    defined in the Item class.
    """
    def condition_description(self):
        return super().condition_description()

    """
    This method personalizes the output for when 
    str() is called, and returns the provided message.
    """
    def __str__(self):
        return f"A gadget full of buttons and secrets."
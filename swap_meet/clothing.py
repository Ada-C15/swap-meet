from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition=0):
        super().__init__(category="Clothing")
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        if self.condition == 5:
            return "Practically just purchased."
        elif self.condition == 4:
            return "A few frayed ends but looks great."
        elif self.condition == 3:
            return "I think you can get the smell out with a good vinegar soak."
        elif self.condition == 2:
            return "If you tie-dye it, you won't even notice the pit stains!"
        elif self.condition == 1:
            return "Hahaha! Oh wait, seriously? You want this??"
        else:
            return "if you wear this, your probably should throw it and yourself in the garbage."
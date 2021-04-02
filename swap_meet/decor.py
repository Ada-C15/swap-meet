from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition=0):
        super().__init__(category="Decor")
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        if self.condition == 5:
            return "Practically just purchased."
        elif self.condition == 4:
            return "A few scratches but looks great."
        elif self.condition == 3:
            return "There's a big crack on one side, but duct tape should fix that."
        elif self.condition == 2:
            return "Hmm. I don't remember this always looking this bad..."
        elif self.condition == 1:
            return "Hahaha! Oh wait, seriously? You want this??"
        else:
            return "Please, for the love of god, don't put this in your home."
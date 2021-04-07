from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition=0):
        super().__init__(category="Electronics")
        self.condition = condition

    def __str__(self):
        return "A gadget full of buttons and secrets."  

    def condition_description(self):
        if self.condition == 5:
            return "Practically just purchased."
        elif self.condition == 4:
            return "A few scratches but works perfecly."
        elif self.condition == 3:
            return "Sometimes you need to shake it to get it to work..."
        elif self.condition == 2:
            return "I dropped it in the toilet but soaked it in rice, so it still sort of works. "
        elif self.condition == 1:
            return "Hahaha! Oh wait, seriously? You want this??"
        else:
            return "I'm so glad you are going to salvage the parts."
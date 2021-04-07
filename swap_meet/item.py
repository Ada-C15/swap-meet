class Item:
    def __init__(self, category = ""):
        # default parameter is what we want in case nothing is passed
        self.category = category

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5:
            return "This fit is fire"
        elif self.condition == 4:
            return "Issa mood"
        elif self.condition == 3:
            return "Yay, we love basics"
        elif self.condition == 2:
            return "I'm feeling meh"
        elif self.condition == 1:
            return "I want to burn these clothes"
        elif self.condition == 0:
            return "I hate it here"



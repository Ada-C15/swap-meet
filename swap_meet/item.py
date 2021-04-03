
class Item:
    def __init__(self, category='', condition=0): #an inventory has to be passed in
        self.category = category
        self.condition = condition
        #self.get_by_category
    def __str__(self):
        return 'Hello World!'

    def condition_description(self):
        # for items in self.category:
            if self.condition == 0:
                return "You probably want to use a glove for this one"
            if self.condition == 1:
                return "Heavily used."
            if self.condition == 2:
                return "Heavily used."
            if self.condition == 3:
                return "Standard wear and tear."
            if self.condition == 4:
                return "*Almost* like new."
            if self.condition == 5:
                return "Like new"
            else:
                return "nope"


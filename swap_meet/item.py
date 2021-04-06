class Item:
    def __init__(self, category='', condition=0):
        # if category is None:
        #     self.category = ""
        # else:
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
        # return self.category

    def condition_description(self):
        description = ""
        if self.condition == 0:
            description = "Seems uselesss, unless ..."
        elif self.condition == 1:
            description = "Happy if you can give it a try!"
        elif self.condition == 2:
            description = "Used - Fair"
        elif self.condition == 3:
            description = "Used - Good"
        elif self.condition == 4:
            description = "Used - Like new"
        elif self.condition == 5:
            description = "New"
        return description

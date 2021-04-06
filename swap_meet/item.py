class Item():
    def __init__(self, category = None, condition = 0):
        
        if category == None:
            self.category = ""
        elif type(category) != str:
            self.category = None
        else:
            self.category = category

        self.condition = condition

    def __str__(self):
        return "Hello World!"
        
    def condition_description(self):

        item_condition = ""

        if self.condition == 0:
            item_condition = "The finest clothing you could wear"
            return item_condition
        elif self.condition >= 1 and self.condition < 2:
            item_condition = "Pretty shabby"
            return item_condition
        elif self.condition >= 2 and self.condition < 3:
            item_condition = "Not too shabby"
            return item_condition
        elif self.condition >= 3 and self.condition < 4:
            item_condition = "Moving on up"
            return item_condition
        elif self.condition >= 4 and self.condition <= 5:
            item_condition = "DAAAAANG"
            return item_condition





    
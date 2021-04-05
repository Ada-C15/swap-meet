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
        
    def item_condition(self, condition):
        item_condition = ""
        if condition == 0:
            item_condition = "The finest clothing you could wear"
            return item_condition
        elif condition >= 1 and condition < 2:
            item_condition = "Not bad"
            return item_condition
        elif condition >= 2 and condition < 3:
            item_condition = "Pretty good"
            return item_condition
        elif condition >= 3 and condition < 4:
            item_condition = "Good condition"
            return item_condition
        elif condition >= 4 and condition < 5:
            item_condition = "Great Condition"
            return item_condition





    
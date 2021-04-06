class Item:
    def __init__(self, category = "", condition = 0):
        if category == None:
            self.category = ""
        else:
            self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 5:
            five_condition_description = "Great Condition"
            return five_condition_description
        elif self.condition == 4:
            four_condition_description = "Good Condition"
            return one_condition_description
        elif self.condition == 3:
            three_condition_description = "Okay Condition"
            return one_condition_description
        elif self.condition == 2:
            two_condition_description = "Poor Condition"
            return one_condition_description
        elif self.condition == 1:
            one_condition_description = "Very Poor Condition"
            return one_condition_description


# from swap_meet.vendor import Vendor

# ***WAVE 1/5***
class Item:
    def __init__(self, category=None, condition=0):
        self.category = category
        self.condition = condition
        if category == None:
            self.category = ""
        else:
            self.category = category

# ***WAVE 3***
    def __str__(self):
        return "Hello World!"

# ***WAVE 5***
    def condition_description(self):
        if self.condition == 0:
            return "This is our lowest rating. This trash won't your treasure, trust us"
        elif self.condition == 1:
            return "Poor"
        elif self.condition == 2:
            return "Fair"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 4:
            return "Like New"
        elif self.condition == 5:
            return "This is our highest rating, brand spankin' NEW"

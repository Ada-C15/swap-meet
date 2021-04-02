class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition_decription_summary = ""
        if self.condition >= 5.0:
            condition_decription_summary = "Better than 5G."
        elif self.condition >= 4.0:
            condition_decription_summary = "Alright alright alright."
        elif self.condition >= 3.0:
            condition_decription_summary = "Good."
        elif self.condition >= 2.0:
            condition_decription_summary = "Not bad. But not good."
        else:
            condition_decription_summary = "Bad."
        return condition_decription_summary



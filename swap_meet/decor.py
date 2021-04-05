from swap_meet.item import Item

class Decor:
    def __init__(self, category = "Decor", condition = 0):
            self.category = category 
            self.condition = condition 

    def __str__(self):
        return "Something to decorate your space."

    # def condition_description(self, condition = 0):
    #     self.condition = ["Mint condition!", "Gently used", "Kinda broken but it'll do", "You don't really want this", "Burn it"]
    #     if condition == 5:
    #         return self.condition[0]
    #     elif condition == 4:
    #         return self.condition[1]
    #     elif condition == 3:
    #         return self.condition[2]
    #     elif condition == 2:
    #         return self.condition[3]
    #     elif condition == 1:
    #         return self.condition[4]
    #     return condition 
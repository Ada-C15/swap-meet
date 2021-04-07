class Item:
    def __init__(self, category="", condition = 0):
        self.category = category
        self.condition = float(condition)

    def __str__(self):
        if str(Item):
            return "Hello World!"

    def condition_description(self):
        if self.condition in range(0,1):
            return "it's kinda like when you take stuff to goodwill even when you know it should go in the trash but you just don't have the heart"
        elif self.condition in range(1,2):
            return "you're never going to have the time to fix it in the way you envision, it's going to sit in yr garage for 3 years and yr gonna get rid of it in some spring cleaning purge"
        elif self.condition in range (2,3):
            return "it's alright, but probably won't last much longer"
        elif self.condition in range (3,4):
            return "it is what it is!"
        elif self.condition in range (4,5):
            return "is a good find and the only reason you should pass is cuz you know you don't need another and someone else shouls have the opportunity"
        elif self.condition >= 5:
            return "you'd be dumb not to swoop this! what a find!"



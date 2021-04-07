class Item:
    def __init__(self, age = None, category = "", condition = 0):
        self.age = age
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"    

    def condition_description(self):
        if self.condition == 5:
            return "Pristine, like a waterfall"
        elif 5 > self.condition >=4:
            return "Really freaking nice"
        elif 4 > self.condition >=3:
            return "You should consult your magic 8-ball about this one"
        elif 3 > self.condition >=2:
            return "You sure you want this?"
        elif 2 > self.condition >=1:
            return "I'd think twice about this if I were you"
        elif self.condition <1:
            return "Ewe. Just...ewe"     


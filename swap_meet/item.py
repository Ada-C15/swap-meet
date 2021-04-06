class Item:
    
    def __init__(self, category="", condition=None, age=None):
        if category == "":
            self.category = ""
        else:
            self.category = category
        if condition == None:
            self.condition = 0
        else:
            self.condition = condition 
        if age == None:
            self.age = None
        else:
            self.age = age

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition <= 1:
            return "Don't bother!"
        elif 1 < self.condition <= 2:
            return "Wicked Used"
        elif 2 < self.condition <= 3:
            return "Used"
        elif 3 < self.condition <= 4:
            return "Gently Used"
        else:
            return "Wicked New"

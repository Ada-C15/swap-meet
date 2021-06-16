#Wave 2:
class Item:
    
    def __init__(self, category = "", condition = 0, age =0):
        self.category= category
        self.condition = condition
        self.age = age

#Wave 3:
    def __str__(self):
        return "Hello World!"

#Wave 5:
    def condition_description(self):
        condition_note = ""
        if self.condition >=0 and self.condition <= 2:
            condition_note = "oh no! please throw"
        elif self.condition >2 and self.condition <= 3.5:
            condition_note = "used for a bit but can keep going..."
        elif self.condition >3.5 and self.condition <= 5:
            condition_note = "fresh and new!"
        return condition_note             

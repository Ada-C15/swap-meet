class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):

        if self.condition == 0.0:
            return "Are you sure you want that?"
        elif self.condition <= 1.0:
            return "Came from home with 8 kids & 3 mastiffs."
        elif self.condition <= 2.0:
            return "Could be worse?"
        elif self.condition <= 3.0:
            return "Meh..."
        elif self.condition <= 4.0:
            return "One heck of a deal!"
        else: 
            return "If you don't take, it's coming home to mama."
        
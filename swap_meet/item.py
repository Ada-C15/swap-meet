class Item:

    def __init__(self, category="", condition=0.0, age=0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello, World!"

    def condition_description(self):
        '''
        Provides a description that corresponds with
        each condition number rating
        '''
        description = ""
        if self.condition < 0 or self.condition > 5:
            return False
        if self.condition == 0:
            description = "Don't trust items without condition descriptions."
        elif self.condition <= 1:
            description = "Janky AF"
        elif self.condition <= 2:
            description = "Poor"
        elif self.condition <= 3:
            description = "Fair"
        elif self.condition <= 4:
            description = "Good"
        elif self.condition <= 5:
            description = "Brand New"
        return description

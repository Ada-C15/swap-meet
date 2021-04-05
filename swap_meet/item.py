class Item:
    def __init__(self, category = '', condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
       return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
             return 'Not available'
        if self.condition == 1:
            return 'Barely Hanging On'
        if self.condition == 2:
            return 'Still usable, but has definely been used'
        if self.condition == 3:
            return 'Normal wear and tear'
        if self.condition == 4:
            return 'This is a real deal swap!'
        if self.condition == 5:
            return 'Minty Fresh'
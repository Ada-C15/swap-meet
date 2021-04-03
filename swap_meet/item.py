class Item:
    def __init__(self, category = '', condition = None):
        self.category = category
        self.condition = condition
    def __str__(self):
       return "Hello World!"
    
    # def condition_description(self):
    #     if condition == None:
    #         return 'Not available'
    #     if condition == 1:
    #         return 'Barely Hanging On'
    #     if condition == 2:
    #         return 'Still usable, but has definely been used'
    #     if condition == 3:
    #         return 'Normal wear and tear'
    #     if condition == 4:
    #         return 'This is a real deal swap!'
    #     if condition == 5:
    #         return 'Minty Fresh'
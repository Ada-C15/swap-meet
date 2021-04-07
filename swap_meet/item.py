# ---- Wave 2 ----- #
class Item:
    '''
    Represents an Item
    Attributes: 
        category (str)
        condition (int/float)
        age (int/float)
    '''

    def __init__(self, category="", condition=0, age=0): 
        '''
        Initializes attributes of Item
        Parameters: 
            category which is optional and empty "" by default
            condition which is optional and 0 by default 
            age which is optional and 0 by default 
        '''
        self.category = category
        self.condition = condition 
        self.age = age

# ---- Wave 3 ----- #
    def __str__(self): 
        '''
        Stringifies an instance of Item 
        '''
        return "Hello World!"

# ---- Wave 5 ----- #
    def condition_description(self):
        '''
        Returns description based on the item's condition
        Returns: 
            description (str) 
        '''
        if self.condition < .9: 
            return "You want this? 🤣"
        elif self.condition < 1.9: 
            return "Great DIY project 🛠" 
        elif self.condition < 2.9: 
            return "Seen better days 👀"
        elif self.condition < 3.9: 
            return "Minty 🌿"
        elif self.condition <= 5.0: 
            return "NEW ✨"

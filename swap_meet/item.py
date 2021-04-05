class Item:
    def __init__(self, category = "", condition = 0, edge = 0):
        self.category = category
        self.condition = condition
        self.edge = edge
    
    '''
    This function is created to customize the string representation 
    of this self instance.
    Python call __str__ method automatically when str() is called,
    then overrides its str() method to return "Hello World!"
    '''
    def __str__(self):
        return "Hello World!"
    

    '''
    This function returns a description of the condition based on
    its value
    '''
    def condition_description(self):
        condition_desc = ""
        if self.condition == 0:
            condition_desc = "No description added"
        elif 1.0 > self.condition > 0.0:
            condition_desc = "You probably prefer to skip this one."
        elif 2.0 > self.condition >= 1.0:
            condition_desc = "Think about the world and recycle! \
No matter the conditions"
        elif 3.0 > self.condition >= 2.0:
            condition_desc = "You can use it for a few more months \
after sanitizing."
        elif 4.0 > self.condition >= 3.0:
            condition_desc = "This will bring joy to your life!"
        elif 5.0 >= self.condition >= 4.0:
            condition_desc = "This one is like NEW! Go for it NOW!"
        return condition_desc









class Clothing:
    def __init__(self, condition = 0, category = "Clothing"):
        self.condition = condition 
        self.category = category
        

    def __str__(self):
        return "The finest clothing you could wear."   

    def condition_description(self):
        return str(self.condition)    
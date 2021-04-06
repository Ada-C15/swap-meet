#from .vendor import Vendor
# ---- Wave 2 ----- #
class Item:
    def __init__(self, category="", condition = 0): 
        self.category = category
        self.condition = condition 

# ---- Wave 3 ----- #
    def __str__(self): 
        return "Hello World!"
    
    # def __repr__(self): 
    #     return f"Item(category='{self.category}')"
        #copy and pasted into ur python code makea  similar object

# ---- Wave 5 ----- #
    def condition_description(self):
        condition_description = ""
        if self.condition < .9: 
            condition_description = "You want this? 🤣"
        elif self.condition < 1.9: 
            condition_description = "Great DIY project 🛠" 
        elif self.condition < 2.9: 
            condition_description = "Seen better days 👀"
        elif self.condition < 3.9: 
            condition_description = "Minty 🌿"
        elif self.condition <= 5.0: 
            condition_description = "NEW ✨"
        return condition_description
# from swap_meet.clothing import Clothing
# from swap_meet.decor import Decor
# from swap_meet.electronics import Electronics

class Item():
    def __init__(self, category ="", condition=0):
        self.category = category
        self.conditon = condition 

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        """
        input: checks the condition of items
        output: the condition of items 

        """
        if self.conditon <= 1:
            return "This is useless and need to recyle."
        elif self.conditon <= 2:
            return "This looks dirty and whole in them so need to clean and sew them before using."
        elif self.conditon <= 3:
            return "This is okay but need to clean them."
        elif self.conditon <= 4:
            return "This is in good condition."
        elif self.condition <= 4.9: 
            return "Basically Brand new."
        else:
            return "Brand new"

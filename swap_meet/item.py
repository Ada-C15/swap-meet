### Wave 2

class Item:
   
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
        return

    def __str__(self) -> str:
        return "Hello World!"


    def condition_description(self):
        conditions = ["Trash, dont buy it!", "Gnarly.\n You might want to clorox this!", "Meh. It's aight!", "Newish. Open box", "Like new. Just buy it", "Mint. Score!"]
        return conditions[self.condition]
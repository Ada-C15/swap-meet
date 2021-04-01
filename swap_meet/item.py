class Item:
    def __init__(self, category=None):
        if category is None:
            category = ""
        self.category = category

    
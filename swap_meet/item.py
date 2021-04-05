class Item:
    def __init__(self, category = "", condition = 0, age = None):
        self.category = category
        self.condition = condition
        #...Optional Enhancement...
        if age is None:
            self.age = 0
        else:
            self.age = age

    def __str__(self):
        return "Hello World!"
        
    def condition_description(self):
        if self.condition == 5:
            return "Brand new! It's a pearl of the closet"
        elif self.condition >= 4:
            return "Very good condition. What a thriftful abudance!"
        elif self.condition >= 3:
            return "This item comes from a home of a pet lover,\
                but our pets donot visit the closet"
        elif self.condition >= 2:
            return "Give it a second chance"
        elif self.condition >= 1:
            return "Noticeable wear and tear"
        else:
            return "Fashionably rustic! But Retro!"

#...Optional Enhancement ...
    def age_description(self):
        if self.age == 0:
            return "BNWOT! Brand New Without Tags"
        elif self.age >= 1 and self.age <= 2.5:
            return "Preloved!"
        elif self.age >= 2.5 and self.age <= 4.5::
            return "Like new. Frugality at its finest"
        else:
            return "Retrospective! Let's say a Vintage"
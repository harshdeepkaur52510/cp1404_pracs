class Guitar:

    def __init__(self, name="Gibson L-5 CES", year=1922, cost=16035.40):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"My guitar: {self.name}, first made in ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        current_year = 2023
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50

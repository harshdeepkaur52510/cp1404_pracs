import csv


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        return self.year < other.year

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"


guitars = []

with open('guitars.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name, year, cost = row
        guitar = Guitar(name, int(year), float(cost))
        guitars.append(guitar)

    for guitar in guitars:
        print(guitar)

    guitars.sort()

    print("Guitars sorted by year:")
    for guitar in guitars:
        print(guitar)

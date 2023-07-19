"""
CP1404
program -> quick_picks
"""
import random

random_numbers = []
MINIMUM_OF_RANGE = 1
MAXIMUM_OF_RANGE = 45

number_of_quick_picks = int(input("How many quick picks? "))

for count in range(number_of_quick_picks):
    for i in range(6):
        number = random.randint(MINIMUM_OF_RANGE, MAXIMUM_OF_RANGE)
        while number in random_numbers:
            number = random.randint(MINIMUM_OF_RANGE, MAXIMUM_OF_RANGE)
        random_numbers.append(number)
    random_numbers = [str(number) for number in random_numbers]
    print(" ".join(sorted(f'{number:>2}' for number in random_numbers)))
    random_numbers = []

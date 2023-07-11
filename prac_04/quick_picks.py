"""
CP1404
program -> quick_picks
"""
import random
number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_pick = random.sample(range(1, 46), 6)
    print(" ".join(map(str, quick_pick)))
"""
files.py
"""
name = input("What is your name? ")
with open("name.txt", "w") as f:
    f.write(name)
with open("name.txt", "r") as f:
    name = f.read()
print(f"Your name is {name}")
with open("numbers.txt", "r") as f:
    num1 = int(f.readline())
    num2 = int(f.readline())
print(f"The sum of the first two numbers is {num1 + num2}")
total = 0
with open("numbers.txt", "r") as f:
    for line in f:
        total += int(line)
print(f"The total of all numbers is {total}")
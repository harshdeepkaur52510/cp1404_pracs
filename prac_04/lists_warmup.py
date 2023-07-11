"""
CP1404
program -> lists_warmup
"""
# Change the first element of numbers to "ten" (the string, not the number 10)
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0] = "ten"
print(numbers)

# Change the last element of numbers to 1
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[-1] = 1
print(numbers)

# Print all the elements from numbers except the first two (slice)
numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[2:])

# Print whether 9 is an element of numbers
numbers = [3, 1, 4, 1, 5, 9, 2]
print(9 in numbers)


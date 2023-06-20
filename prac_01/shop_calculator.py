"""
shop calculator
"""
total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    discount = total * 0.1   # 10% discount
    total -= discount
print(f"Total price for {number_of_items} items is ${total:.2f}")
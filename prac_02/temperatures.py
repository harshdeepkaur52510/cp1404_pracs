"""
Convert Temperature from Celsius to Fahrenheit and Fahrenheit to Celsius
temperatures.py
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_into_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = convert_into_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thankyou")


def convert_into_fahrenheit(celsius):
    """celsius convert into fahrenheit"""
    return celsius * 9.0 / 5 + 32


def convert_into_celsius(fahrenheit):
    """fahrenheit convert into celsius"""
    return 5 / 9 * (fahrenheit - 32)


main()

"""
Conversion of Temperature
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
            fahrenheit = celsius_convert_into_fahrenheit(celsius)
            print(f"Result: {celsius:.2f} C")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = fahrenheit_convert_into_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thankyou")

def celsius_convert_into_fahrenheit(celsius):
    """celsius convert into fahrenheit"""
    return celsius * 9.0 / 5 + 32

def fahrenheit_convert_into_celsius(fahrenheit):
    """fahrenheit convert into celsius"""
    return 5 / 9 * (fahrenheit - 32)

main()


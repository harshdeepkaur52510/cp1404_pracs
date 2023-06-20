"""
Password stars Program
"""
MINIMUM_LENGTH = 4

def main():
    """Get and print password in form of stars"""
    password = get_password()
    print_password_stars(password)

def get_password():
    """Get password of minimum length"""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid Input")
        password = input("Enter password: ")
    return password


def print_password_stars(password):
    for _ in range(len(password)):
        print("*", end="")


main()
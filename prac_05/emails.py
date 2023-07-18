"""
emails.py
"""


def main():
    name_from_email_dict = {}
    email = input("Enter your Email: ")
    while email != "":
        name = name_from_email(email)
        confirm = input(f"Is your name {name}? (Y/n): ")
        if confirm.upper() != "Y" and confirm != "":
            name = input("Enter your name: ")
            name_from_email_dict[email] = name

        email = input("Enter your Email: ")

    for email, name in name_from_email_dict.items():
        print(f"{name} {email}")


def name_from_email(email):
    prefix = email.split('@')[0]
    parts = prefix.replace('.', '')
    name = " ".join(parts.split()).title()
    return name


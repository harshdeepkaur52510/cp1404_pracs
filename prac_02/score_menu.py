"""
score menu
score_menu.py
"""
import random


def get_valid_score():
    flag = 1
    while flag:
        try:
            score = int(input("Enter a valid score (0-100 inclusive): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid score.")


def get_result(score):
    """Get result status"""
    if score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Show stars"""
    for _ in range(score):
        print("*", end="")
    print()


def main():
    flag = 1;
    print("Welcome to the Score Program!")

    while flag == 1:
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if 'score' in locals():
                result = get_result(score)
                print("Result:", result)
            else:
                print("No score entered. Please select (G)et a valid score first.")
        elif choice == "S":
            if 'score' in locals():
                show_stars(score)
            else:
                print("No score entered. Please select (G)et a valid score first.")
        elif choice == "Q":
            print(" Thank you for using the Score Program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()

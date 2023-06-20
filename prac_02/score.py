"""
Determine the score
"""
def main():
    """Get score in numbers and display the result"""
    score = float(input("Enter score: "))
    print(get_results(score))


def get_results(score):
    """Determine the status of score"""
    if score < 0 or score > 100:
        return"Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return"Passable"
    else:
        return"Bad"

main()
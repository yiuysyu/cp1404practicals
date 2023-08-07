def main():
    score = get_valid_value()

    menu = """Menu:
    (G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit"""

    choice = ""

    while choice != "Q":
        print(menu)
        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_value()
        elif choice == "P":
            result = get_result(score)
            print(f"Your result is: {result}")
        elif choice == "S":
            print_stars(score)
        elif choice == "Q":
            print("Farewell")
        else:
            print("Invalid score")


def get_valid_value():
    while True:
        score = float(input("Your score:"))
        if 0 <= score <= 100:
            return score
        else:
            print("Invalid score")


def get_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    print("*" * int(score))


main()


import random


def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    user_score = float(input("Enter your score: "))
    user_result = calculate_result(user_score)
    print(user_result)

    random_score = random.randint(0, 100)
    random_result = calculate_result(random_score)
    print(f"Your random Score is: {random_score}, Your result is: {random_result}")


main()

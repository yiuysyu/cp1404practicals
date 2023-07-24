"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the thing user enter is not an integer.
2. When will a ZeroDivisionError occur?
When user enter 0 as denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes.
"""
while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        if denominator == 0:
            print("Cannot divide by zero! Please enter again:")
        else:
            fraction = numerator / denominator
            print(fraction)
            break

    except ValueError:
        print("Numerator and denominator must be valid numbers!")

print("Finished.")


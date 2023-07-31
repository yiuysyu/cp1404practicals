import random
RANDOM_NUMBERS = 6
MINIMUM_VALUE = 1
MAXIMUM_VALUE = 45
number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    quick_pick = sorted(random.sample(range(MINIMUM_VALUE, MAXIMUM_VALUE + 1), RANDOM_NUMBERS))
    print(" ".join(f"{number:2}" for number in quick_pick))

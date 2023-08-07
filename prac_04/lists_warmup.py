numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0]
output: 3

numbers[-1]
output: 2

numbers[3]
output: 1

numbers[:-1]
output: 3, 1, 4, 1, 5, 9

numbers[3:4]
output: 1

5 in numbers
output: True

7 in numbers
output: False

"3" in numbers
output: False

numbers + [6, 5, 3]
output: 3, 1, 4, 1, 5, 9, 2, 6, 5, 3
"""

# 1 Change the first element of numbers to "ten"
numbers[0] = "ten"

# 2 Change the last element of numbers to 1
numbers[-1] = 1

# 3 Print all the elements from numbers except the first two (slice)
print(numbers[2:len(numbers)])

# 4 Print whether 9 is an element of numbers
print(9 in numbers)

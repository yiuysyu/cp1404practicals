# 1
user_name = input("What is your name? ")
with open("name.txt", "w") as file:
    file.write(user_name)

# 2
with open("name.txt", "r") as file:
    user_names = file.read()
    print(user_names)

# 3
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    result = first_number + second_number
    print(result)

# 4
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line)
        total += number
print(total)

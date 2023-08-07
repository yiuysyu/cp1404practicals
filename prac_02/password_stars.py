def main():
    # Set minimum number of password
    min_password_length = 8

    # Get password from the user
    password = get_password(min_password_length)

    # Print stars
    print_stars(password)


def get_password(min_length):
    while True:
        password = input("Enter your password: ")

        if len(password) < min_length:
            print(f"Password should be at least {min_length} characters long. Try again.")
        else:
            return password


def print_stars(password):
    print("*" * len(password))


main()

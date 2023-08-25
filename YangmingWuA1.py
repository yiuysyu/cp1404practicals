"""
Name: Yangming Wu
Date started: 22/08/2023
GitHub URL:
"""
import random

# List the constants
VISITED = 'v'
UNVISITED = 'n'
FILENAME = 'places.csv'


# Read the file
def read_file(file_name):
    places = []
    with open(file_name, 'r') as file:
        for line in file:
            name, country, priority, visit_status = line.strip().split(',')
            places.append([name, country, int(priority), visit_status])
    return places


# Sort the places by priority in ascending order, and unvisited places come first
def sort_places(place):
    return place[3], place[2]


# Display the list of places
def display_places(places):
    print("Places:")
    places.sort(key=sort_places)

    for i, place in enumerate(places, start=1):
        visit_status = '*' if place[3] == UNVISITED else ' '
        # Display list of places with the space between name, country, and priority
        print(f"{visit_status}{i}. {place[0]:<8} in {place[1]:<13} {place[2]}")

    unvisited_number = sum(1 for place in places if place[3] == UNVISITED)
    total_places = len(places)

    # Check if the number of unvisited place is zero
    if unvisited_number > 0:
        print(f"{total_places} places. You still want to visit {unvisited_number} places.")
    else:
        print(f"{total_places} places.No places left to visit. Why not add a new place? ")


# Recommend a random and also unvisited place to user
def recommend_random_place(places):
    unvisited_places = [place for place in places if place[3] == UNVISITED]
    if not unvisited_places:
        print("No places left to visit!")
    else:
        random_place = random.choice(unvisited_places)
        print(f"Not sure where to visit next?\nHow about... {random_place[0]} in {random_place[1]}?")


# Add new place to the file
def add_place(places, name, country, priority):
    places.append([name, country, int(priority), UNVISITED])
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")


# Mark places which has already visited
def mark_visited(places, index):
    if places[index - 1][3] == VISITED:
        print(f"You have already visited {places[index - 1][0]}")

    else:
        places[index - 1][3] = VISITED
        print(f"{places[index - 1][0]} in {places[index - 1][1]} visited!")


# Save data to the file
def save_data(file_name, places):
    with open(file_name, 'w') as file:
        for place in places:
            file.write(f"{place[0]},{place[1]},{place[2]},{place[3]}\n")


# Get valid input
def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input can not be blank")
        else:
            return user_input


# Main code
def main():
    # Load data from the file
    places = read_file(FILENAME)

    # Display welcome messages
    print("Travel Tracker 1.0 - by Yangming Wu")
    print(f"{len(places)} places loaded from {FILENAME}")

    while True:
        # Display the menu
        print("Menu:")
        print("L - List places")
        print("R - Recommend random place")
        print("A - Add new place")
        print("M - Mark a place as visited")
        print("Q - Quit")

        choice = input(">>> ").strip().lower()

        # List all the places
        if choice == 'l':
            display_places(places)

        # Recommend a random place for user
        elif choice == 'r':
            recommend_random_place(places)

        # Add a new place
        elif choice == 'a':
            while True:
                # get name, country, and priority from user
                name = get_valid_input("Name: ")
                country = get_valid_input("Country: ")
                priority = get_valid_input("Priority: ")

                add_place(places, name, country, priority)
                break

        # Mark place when already visited
        elif choice == 'm':
            # Check if there is unvisited place left
            unvisited_number = sum(1 for place in places if place[3] == UNVISITED)
            if unvisited_number <= 0:
                print("No places left to visit!")

            else:
                display_places(places)
                print("Enter the number of a place to mark as visited: ")
                while True:
                    try:
                        chosen_number = int(input(">>> "))
                        # Check if the user input greater than zero
                        if chosen_number <= 0:
                            print("Number must be > 0")
                        # Check if the user input in the list of places
                        elif chosen_number < 1 or chosen_number > len(places):
                            print("Invalid place number")
                        else:
                            break
                    # Check if the user input an integer
                    except ValueError:
                        print("Invalid input; enter a valid number")
                mark_visited(places, int(chosen_number))

        # End the program
        elif choice == 'q':
            save_data(FILENAME, places)
            print(f"{len(places)} places saved to {FILENAME}")
            print("Have a nice day :)")
            break

        # Invalid menu options
        else:
            print("Invalid menu choice")


if __name__ == "__main__":
    main()

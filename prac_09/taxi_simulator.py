from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    """Display the taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def main():
    # List of taxi
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    total_bill = 0
    current_taxi = None

    print("Let's drive!")

    while True:
        # Display the menu
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").strip().lower()

        if user_choice == 'q':
            break

        elif user_choice == 'c':
            display_taxis(taxis)
            taxi_choice = input("Choose taxi: ").strip()
            taxi_choice = int(taxi_choice)
            if 0 <= taxi_choice < len(taxis):
                current_taxi = taxis[taxi_choice]
            else:
                print("Invalid taxi choice")

        elif user_choice == 'd':
            drive_distance = float(input("Drive how far? "))
            trip_cost = current_taxi.drive(drive_distance)
            total_bill += trip_cost
            print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


if __name__ == '__main__':
    main()

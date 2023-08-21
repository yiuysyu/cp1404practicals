from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

    print("\n... snip ...""\nThese are my guitars:")
    current_year = 2023

    for number, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage(current_year) else ""
        print(f"Guitar {number}: {guitar.name} ({guitar.year}), worth ${guitar.cost:.2f}{vintage_string}")


main()

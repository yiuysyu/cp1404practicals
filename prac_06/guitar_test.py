from guitar import Guitar


def test_get_age():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1111.0)

    expected_gibson_age = 100
    actual_gibson_age = gibson.get_age(2022)
    print(f"{gibson.name} get_age() - Expected {expected_gibson_age}. Got {actual_gibson_age}")

    expected_another_guitar_age = 9
    actual_another_guitar_age = another_guitar.get_age(2022)
    print(f"{another_guitar.name} get_age() - Expected {expected_another_guitar_age}. Got {actual_another_guitar_age}")


def test_is_vintage():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1111.0)

    expected_gibson_vintage = True
    actual_gibson_vintage = gibson.is_vintage(2022)
    print(f"{gibson.name} is_vintage() - Expected {expected_gibson_vintage}. Got {actual_gibson_vintage}")

    expected_another_guitar_vintage = False
    actual_another_guitar_vintage = another_guitar.is_vintage(2022)
    print(
        f"{another_guitar.name} is_vintage() - Expected {expected_another_guitar_vintage}. "
        f"Got {actual_another_guitar_vintage}")


def main():
    print("Test get_age:")
    test_get_age()

    print("Test is_vintage:")
    test_is_vintage()


main()

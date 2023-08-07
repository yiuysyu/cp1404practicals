"""
Wimbledon
Estimate: 60 minutes
Actual:   65 minutes
1
"""


def main():
    data = read_file("wimbledon.csv")

    number_of_champions = count_champions(data)
    print("Wimbledon Champions:")
    for champion, count in number_of_champions.items():
        print(f"{champion} {count}")

    countries = get_countries(data)
    countries_list = ', '.join(countries)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(countries_list)


def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
        return [line.strip().split(',') for line in lines[1:]]


def count_champions(data):
    number_of_champions = {}
    for row in data:
        champion = row[2]
        number_of_champions[champion] = number_of_champions.get(champion, 0) + 1
    return number_of_champions


def get_countries(data):
    countries = set(row[1] for row in data)
    return sorted(countries)


main()

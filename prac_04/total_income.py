"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def get_incomes(number_of_months):
    """Get income and put it in list."""
    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    return incomes


def print_income_report(incomes_list):
    """Display the income report."""
    total = 0
    print("Income Report\n-------------")
    for month, income in enumerate(incomes_list, start=1):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def main():
    """Display income report for incomes over a given number of months."""
    number_of_months = int(input("How many months? "))
    incomes = get_incomes(number_of_months)
    print_income_report(incomes)


main()

while True:
    number_of_items = int(input("Number of items: "))
    if number_of_items >= 0:
        break
    print("Invalid number of items!")

total_price = 0

for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount

print(f"Total price for {number_of_items} items is ${total_price:.2f}")


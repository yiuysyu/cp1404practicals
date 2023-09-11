from prac_09.unreliable_car import UnreliableCar

my_unreliable_car = UnreliableCar("UnreliableCar", 100, 50)

# Drive for 30 km
distance_driven = my_unreliable_car.drive(30)

# Display the result
if distance_driven > 0:
    print(f"Car drove {distance_driven} km.")
else:
    print("Car didn't start.")

# Test
for i in range(5):
    distance_driven = my_unreliable_car.drive(30)
    if distance_driven > 0:
        print(f"Attempt {i + 1}: Car drove {distance_driven} km.")
    else:
        print(f"Attempt {i + 1}: Car didn't start.")

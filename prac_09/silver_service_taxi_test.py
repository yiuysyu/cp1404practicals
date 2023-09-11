from prac_09.silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi object
my_silver_taxi = SilverServiceTaxi("Hummer", 200, 2)

# Drive the taxi for 18 km
my_silver_taxi.drive(18)

# Display the fare
fare = my_silver_taxi.get_fare()
print(f"Total fare: ${fare:.2f}")

# Display the details
print(my_silver_taxi)

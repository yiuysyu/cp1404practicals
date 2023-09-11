# Import the class
from prac_09.taxi import Taxi

# Create a new taxi object
my_taxi = Taxi("Prius 1", 100)

# Drive the taxi 40 km
my_taxi.drive(40)

# Display the taxi's details and the current fare
print(f"Taxi details: {my_taxi}")
print(f"Current fare: ${my_taxi.get_fare():.2f}")

# Restart the meter (start a new fare)
my_taxi.start_fare()

# Drive the car 100 km
my_taxi.drive(100)

# Display the updated details and the current fare
print(f"Taxi details: {my_taxi}")
print(f"Current fare: ${my_taxi.get_fare():.2f}")

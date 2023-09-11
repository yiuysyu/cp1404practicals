from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialized version of a Car with reliability for driving."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        # Get random number between 0 and 100
        random_number = random.randint(0, 100)

        if random_number < self.reliability:
            # Random number less than reliability
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            # Random number greater or equal to reliability
            return 0

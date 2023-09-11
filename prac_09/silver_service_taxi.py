from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialized version of a Taxi for silver service."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Customize self.price_per_km based on fanciness
        self.price_per_km *= self.fanciness

    def get_fare(self):
        """Return the price for the taxi trip, including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like Taxi but with fanciness and flagfall."""
        return f"{super().__str__()},  plus flagfall of ${self.flagfall:.2f}"

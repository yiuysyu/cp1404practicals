class Band:

    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        musician_strs = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strs)})"

    def add_musician(self, musician):
        """Add new musician."""
        self.musicians.append(musician)

    def play(self):
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)


if __name__ == '__main__':
    from musician import Musician
    from guitar import Guitar

    # Create Guitarists
    nuno = Musician("Nuno Bettencourt")
    nuno.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno.add(Guitar("Takamine acoustic", 1986, 1200.00))

    gary = Musician("Gary Cherone")

    pat = Musician("Pat Badger")
    pat.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.00))

    kevin = Musician("Kevin Figueiredo")

    # Create Band and add Musicians
    extreme = Band("Extreme")
    extreme.add_musician(nuno)
    extreme.add_musician(gary)
    extreme.add_musician(pat)
    extreme.add_musician(kevin)

    # Display Band and have them play
    print(extreme)
    print(extreme.play())

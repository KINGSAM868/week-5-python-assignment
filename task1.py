# Superhero Base Class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, guardian of {self.city}! 💥")

    def use_power(self):
        print(f"{self.name} uses {self.power}! ⚡")

# Subclass with inheritance
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} soars at {self.flight_speed} km/h while unleashing {self.power}! 🦸‍♂️")

# Another subclass
class TechHero(Superhero):
    def __init__(self, name, power, city, gadgets):
        super().__init__(name, power, city)
        self.gadgets = gadgets

    def use_power(self):
        print(f"{self.name} uses high-tech gadgets ({', '.join(self.gadgets)}) to perform {self.power}! 🤖")

# Testing
if __name__ == "__main__":
    hero1 = FlyingHero("Skyblade", "Wind Slash", "Metropolis", 900)
    hero2 = TechHero("Gearmaster", "Laser Barrage", "Neo-Tokyo", ["Drone", "Exo-suit"])

    hero1.introduce()
    hero1.use_power()

    hero2.introduce()
    hero2.use_power()


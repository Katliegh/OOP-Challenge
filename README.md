Pet.py

class DigitalPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food.")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good nap.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played and had fun!")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print(f"Status of {self.name}:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f" - {trick}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")




 Main.py
 from pet import DigitalPet

# Create the pet
sipho = DigitalPet("Sipho")

# Call methods to test functionality
sipho.get_status()
sipho.eat()
sipho.sleep()
sipho.play()
sipho.train("roll over")
sipho.train("sit")
sipho.show_tricks()
sipho.get_status()

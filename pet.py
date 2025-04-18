class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger -= 3
        if self.hunger < 0:
            self.hunger = 0
        self.happiness += 1
        if self.happiness > 10:
            self.happiness = 10

    def sleep(self):
        self.energy += 5
        if self.energy > 10:
            self.energy = 10

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness += 2
            if self.happiness > 10:
                self.happiness = 10
            self.hunger += 1
            if self.hunger > 10:
                self.hunger = 10

    def get_status(self):
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def train(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(trick)
        else:
            print(f"{self.name} doesn't know any tricks yet.")
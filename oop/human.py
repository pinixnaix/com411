import oop.human


class Human:

    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Human"
        self.age = 0
        self.energy = Human.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'Human(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f'Human {self.name} is {self.age} years old and has {self.energy}% energy!'

    def grow(self):
        self.age += 1

    def eat(self, amount):
        if amount + self.energy <= oop.human.Human.MAX_ENERGY:
            self.energy += amount

    def move(self, distance):
        if self.energy - distance >= 0:
            self.energy -= distance


if __name__ == "__main__":
    human = Human()
    human.display()

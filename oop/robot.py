class Robot:
    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Robot"
        self.age = 0
        self.energy = 0

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'Robot(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f'Robot {self.name} is {self.age} years old and has {self.energy}% energy!'


if __name__ == "__main__":
    robot = Robot()
    robot.display()

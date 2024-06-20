# a simple python program  to demonstrate encapsulation in oop

class Toy:
    def __init__(self, name):
        self.name = name  # Public attribute

    def play(self):
        print(f"I'm playing with my {self.name}!")


# Creating an instance of Toy
my_toy = Toy("Teddy Bear")

# Accessing and using the toy
my_toy.play()

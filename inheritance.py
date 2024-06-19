
# parent class/base class/super class
class animal:
    hasScales = True

    def sound(self):
        print("animal is speaking")

# child class/sub class/derived class
class duck(animal):
    hasWings = True
    def move(self):
        print("duck is swimming")

class Caterpillar(duck):
    def move(self):
        print("Caterpillar is slithering")

a = animal()

d = duck()
print(d.hasWings)

c = Caterpillar()
c.sound()

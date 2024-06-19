# class is a blueprint of an object
# object is an instance of a class

class Person:
    # properties/attributes/variables/characteristics
    name = "james"
    age = 23
    gender = "male"

    # methods/function/behaviour
    def move(self):
        print("person is walking")


farmer = Person()
farmer.move()
print(farmer.gender)

doctor = Person()


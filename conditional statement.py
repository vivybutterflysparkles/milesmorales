
temperature = 46

if temperature < 25:
    print("it is cold")
elif temperature > 25:
    print("it is hot")
else:
    print("normal temperature")

# simple program to return the largest number among three numbers
first = 90
second = 45
third = 69
if first > second and first > third:
    print(first, "is the largest number")
elif second > first and second > third:
    print(second,"is the largest number")
else:
    print(third,"is the largest number")

# write a python program that checks whether a number is even or odd
x = 2
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")



number = 10
if number == 0:
    print(number, "is neutral")
elif number % 2 ==0:
    print(number, "is even")
else:
    print(number, "is odd")
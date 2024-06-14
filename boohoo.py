numbers = []
for i in range(4):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
smallest = numbers[0]
for num in numbers:
        if num < smallest:
            smallest = num
print("The smallest number is:", smallest)

# write a python program that checks the smallest number in an array of numbers
first = int(input("first number :"))
second = int(input("second number :"))
third = int(input("third number :"))
fourth = int(input("fourth number :"))

if first < second and first < third and first < fourth:
    print(first, "is the smallest number")
elif second < first and second < third and second < fourth:
    print(second,"is the smallest number")
elif third < second and third < first and third < fourth:
    print(third, "is the smallest")
else:
    print(fourth, "is the smallest number")



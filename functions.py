# inbuilt function /  standard library functions

y = min(23, 56, 1000, 5647)
print(y)

x = max(90, 2, 76, 14)
print("the maximum number is", x)

z = pow(2, 3)
print(z)

# user-defined functions
def school():
    print("eMobilis")
school() # calling a function

def multiply():
    num1 = 5
    num2 = 6
    print(num1 * num2)
multiply()

# parameters and arguments
def add(a, b):
    print(a + b)
add(5, 66)
add(15, 67)
add(25, 69)
add(35, 62)

def employee(fullname,age,salary,phone,position):
    print(fullname,age,salary,phone,position)
employee("John KAMAU",23,56000,114298238,"MD")
employee("VIVIAN opindi",19,28000,113467258,"AS")
employee("JAMES KIMEMIA",29,98000,113812854,"PA")
employee("JAMO KUIRI",45,198000,133421854,"AM")
employee("MATILDO KIRUBI",35,18000,123521854,"DEP")

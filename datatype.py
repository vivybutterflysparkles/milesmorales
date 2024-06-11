# datatype
number = 78  # Int
num = 45.90  # Float
greeting = "how are you doing?"  # str
is_Programming_Interesting = True  #bool
devices = ["laptop","computer","phone", "tablet"] # List
browsers = ("Firefox","Chrome","Safari","brave")  # Tuple
countries = {"kenya","uganda","tanzania"} # Set
employee = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@gmail.com",
    "age": 23,
    "gender": "male",
    "nationality": "british",
} # Dictionary
print(num)
print(is_Programming_Interesting)
print(employee["first_name"])
print(countries)

# Determining a data type
print(type(countries))
print(type(employee))

# Typecasting is the process of converting one datatype to another
print(int(num))
print(float(number))

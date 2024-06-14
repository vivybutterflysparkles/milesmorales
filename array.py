
courses = ["computer science", "it", "bit", "software engineering"]

print(courses)

#  accessing an element in an array
print(courses[2])

# looping through an array
for x in courses:
    print(x)

# adding a new element into an array
courses.append("data science")
print(courses)

# deleting an element in an array
courses.remove("it")
print(courses)
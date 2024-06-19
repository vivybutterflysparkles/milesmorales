class student:

    def __init__(self,firstname,course,gender):
        self.firstname = firstname
        self.course = course
        self.gender = gender

    def study(self):
        print(self.firstname, "is studying")

student1 = student("John","MIT","Male")
student1.study()
student2 = student("vivian","cybersecurity","Female")
student2.study()
student3 = student("Jack","datascience","Male")
student3.study()

class Student:
    def __init__(self, name, school, grade):
        self.name = name
        self.school = school
        self.grade = grade

    def out_info(self):
        print("Name : %s" % self.name)
        print("School : %s" % self.school)
        print("Grade : %s" % self.grade)

name, school, grade = input().split()

info = Student(name, school, grade)
info.out_info()
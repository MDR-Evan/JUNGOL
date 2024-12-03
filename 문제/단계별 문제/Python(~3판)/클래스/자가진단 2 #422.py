class School:
    jeju = "Jejuelementary"
    grade = 6

    def __init__(self, school, grade):
        self.school = school
        self.grade = grade

    def out_info(self):
        print("%d grade in %s School" % (School.grade, School.jeju))
        print("%d grade in %s School" % (self.grade, self.school))

school, grade = input().split()

data = School(school, int(grade))

data.out_info()